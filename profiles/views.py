from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


@login_required
def profile(request):
    """
    Display and update the user's profile.

    Retrieves the UserProfile instance associated with the current user.
    Handles form submission for updating the profile information.
    Displays the user's order history.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered profile page template with user profile data.
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders_linked.all()

    template = "profiles/profile.html"
    context = {
        "user": request.user,  # Provide user object for displaying user's name 
        "form": form,
        "orders": orders,
        "on_profile_page": True,
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    """
    Display details of a specific order from the user's order history.

    Retrieves the Order instance based on the provided order number.
    Displays a confirmation message regarding the order.

    Args:
        request (HttpRequest): The HTTP request object.
        order_number (str): The order number to retrieve details for.

    Returns:
        HttpResponse: Rendered order history template with order details.
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(
        request,
        (
            f"This is a past confirmation for order number {order_number}. "
            "A confirmation email was sent on the order date."
        ),
    )

    template = "checkout/checkout_success.html"
    context = {
        "order": order,
        "from_profile": True,
    }

    return render(request, template, context)
