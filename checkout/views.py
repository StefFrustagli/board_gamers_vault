from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from django.urls import reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from marketplace.models import Game
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from bag.contexts import bag_contents

import stripe
import json

stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
@require_POST
def cache_checkout_data(request):
    """
    Cache checkout data for processing payment.

    This view modifies the Stripe PaymentIntent metadata with bag contents,
    save_info preference, and username before processing the payment.

    Args:
        request (HttpRequest): The HTTP request object containing POST data.

    Returns:
        HttpResponse: HTTP response indicating success or error status.
    """
    try:
        pid = request.POST.get("client_secret").split("_secret")[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(
            pid,
            metadata={
                "bag": json.dumps(request.session.get("bag", {})),
                "save_info": request.POST.get("save_info"),
                "username": request.user,
            },
        )
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(
            request,
            "Sorry, your payment cannot be \
            processed right now. Please try again later.",
        )
        return HttpResponse(content=e, status=400)


@login_required
def checkout(request):
    """
    Handle the checkout process.

    This view handles the rendering of the checkout page,
    ensuring that the user has items in their bag before proceeding.
    If the bag is empty, an error message is displayed,
    and the user is redirected to the products page.
    Otherwise, an order form is created and rendered on the checkout page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object with
        the rendered checkout template.
    """
    # Retrieve Stripe TEST keys from settings
    stripe_public_key = settings.STRIPE_TEST_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_TEST_SECRET_KEY

    # Initialize intent to None to handle both GET and POST requests
    intent = None

    # Set the Stripe API key
    stripe.api_key = stripe_secret_key

    if request.method == "POST":
        # Get the shopping bag from the session
        bag = request.session.get("bag", {})

        # Collect form data from the POST request
        form_data = {
            "full_name": request.POST["full_name"],
            "email": request.POST["email"],
            "phone_number": request.POST["phone_number"],
            "country": request.POST["country"],
            "postcode": request.POST["postcode"],
            "town_or_city": request.POST["town_or_city"],
            "street_address1": request.POST["street_address1"],
            "street_address2": request.POST["street_address2"],
            "county": request.POST["county"],
        }

        # Create an order form instance with the collected data
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            # Save the order form to create an Order instance
            order = order_form.save(commit=False)
            pid = request.POST.get("client_secret").split("_secret")[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            for item_id, quantity in bag.items():
                try:
                    # Retrieve the game from the database
                    game = Game.objects.get(id=item_id)
                    # Create an OrderLineItem for each game in the bag
                    order_line_item = OrderLineItem(
                        order=order,
                        game=game,
                        quantity=quantity,
                    )
                    order_line_item.save()
                except Game.DoesNotExist:
                    # Handle the case where a game is not found
                    messages.error(
                        request,
                        (
                            "One of the products in your bag wasn't found \
                            in our database. "
                            "Please call us for assistance!"
                        ),
                    )
                    order.delete()  # Delete the order if a game is not found
                    return redirect(reverse("view_bag"))

            # Store the 'save_info' preference in the session
            request.session["save_info"] = "save-info" in request.POST
            return redirect(reverse(
                "checkout_success", args=[order.order_number]
            ))
        else:
            # Handle the case where the order form is not valid
            messages.error(
                request,
                "There was an error with your form. \
                Please double check your information.",
            )
    else:
        # Handle the case where the request method is GET
        bag = request.session.get("bag", {})
        if not bag:
            messages.error(request, "There's nothing in your bag")
            return redirect(reverse("games_list"))

        # Calculate the total amount and create a Stripe PaymentIntent
        current_bag = bag_contents(request)
        total = current_bag["grand_total"]
        stripe_total = round(total * 100)
        # Stripe API key
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(
                    initial={
                        "full_name": profile.user.get_full_name(),
                        "email": profile.user.email,
                        "town_or_city": profile.default_town_or_city,
                    }
                )
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:  # Create an empty order form
            order_form = OrderForm()

    # Warning if the Stripe public key is missing
    if not stripe_public_key:
        messages.warning(
            request,
            (
                "Stripe public key is missing. "
                "Did you forget to set it in your environment?"
            ),
        )

    # Template to be rendered
    template = "checkout/checkout.html"

    # Context to be passed to the template
    context = {
        "order_form": order_form,
        "stripe_public_key": stripe_public_key,
        "client_secret": intent.client_secret,
    }

    return render(request, template, context)


@login_required
def checkout_success(request, order_number):
    """
    Handle successful checkouts.

    This view handles the rendering of the checkout success page,
    displays a success message, and clears the shopping bag from the session.

    Args:
        request (HttpRequest): The HTTP request object.
        order_number (str): Order number of the successfully processed order.

    Returns:
        HttpResponse:
        The HTTP response object with the rendered checkout success template.
    """
    save_info = request.session.get("save_info")
    order = get_object_or_404(Order, order_number=order_number)
    # Add the availability condition here
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                "default_phone_number": order.phone_number,
                "default_country": order.country,
                "default_postcode": order.postcode,
                "default_town_or_city": order.town_or_city,
                "default_street_address1": order.street_address1,
                "default_street_address2": order.street_address2,
                "default_county": order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    # Set is_available to False for each product in the order's line items
    for line_item in order.lineitems.all():
        game = line_item.game
        game.is_available = False
        game.save()

    messages.success(
        request,
        f"Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.",
    )

    if "bag" in request.session:
        del request.session["bag"]

    template = "checkout/checkout_success.html"
    context = {
        "order": order,
    }

    return render(request, template, context)
