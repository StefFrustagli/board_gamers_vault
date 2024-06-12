from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from marketplace.models import Game
from bag.contexts import bag_contents

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request):
    """
    Handle the checkout process.

    This view handles the rendering of the checkout page, ensuring that the user 
    has items in their bag before proceeding. If the bag is empty, an error message 
    is displayed, and the user is redirected to the products page. Otherwise, an 
    order form is created and rendered on the checkout page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object with the rendered checkout template.
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
            order = order_form.save()
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
                    # Handle the case where a game is not found in the database
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
            return redirect(reverse("checkout_success", args=[order.order_number]))
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

        # Create an empty order form
        order_form = OrderForm()

    # Warn the user if the Stripe public key is missing TO BE REMOVED
    if not stripe_public_key:
        messages.warning(
            request, 
            (
                'Stripe public key is missing. '
                'Did you forget to set it in your environment?'
                )
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
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
