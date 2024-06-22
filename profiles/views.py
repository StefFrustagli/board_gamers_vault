from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


@login_required
def profile(request):
    """Display and update the user's profile."""
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
        "user": request.user,  # Provide user object for displaying user's name dynamically
        "form": form,
        "orders": orders,
        "on_profile_page": True,
    }

    return render(request, template, context)


# @login_required
# def profile(request):
#     """Display the user's profile."""
#     profile = get_object_or_404(UserProfile, user=request.user)

#     if request.method == "POST":
#         form = UserProfileForm(request.POST, instance=profile)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Profile updated successfully")

#     form = UserProfileForm(instance=profile)
#     orders = profile.orders_linked.all()

#     template = "profiles/profile.html"
#     context = {"form": form,
#                 "orders": orders,
#                 "on_profile_page": True}

#     return render(request, template, context)


# def profile_view(request):
#     user = request.user  # if logged-in user
#     context = {
#         "user": user,
#     }
#     return render(request, "profile.html", context)


def order_history(request, order_number):
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
