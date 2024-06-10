from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


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
    # Get the shopping bag from the session
    bag = request.session.get("bag", {})

    # If the bag is empty, display an error message
    # and redirect to the products page
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse("products"))

    # Initialize an empty order form
    order_form = OrderForm()

    # Template to be rendered
    template = "checkout/checkout.html"

    # Context to be passed to the template
    context = {
        "order_form": order_form,
        "stripe_public_key": "pk_live_51PQ8d704yPJnLEmvZYqB3PoftGQUr0f3Jrh0nrjFfD93GU0FLlPBK8IJIvdTSwpXUiWtaXqjOWqBPQrlGdszq9qt005tCif0bt",
        "client_secret": "test client secret",
    }

    return render(request, template, context)
