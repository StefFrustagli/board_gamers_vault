from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages

from marketplace.models import Game


def view_bag(request):
    """A view that renders the bag contents page"""

    return render(request, "bag/bag.html")


def add_to_bag(request, item_id):
    """Add a quantity of the specified product to the shopping bag"""

    game = get_object_or_404(Game, pk=item_id)

    # Quantity always one as unique item
    quantity = 1

    # Check if the game is available
    if not game.is_available:
        messages.error(request, f"{game.title} is not available anymore.")
        return redirect(
            request.META.get("HTTP_REFERER", "marketplace/")
        )  # Redirect back to the previous page or shop page

    # Retrieve the redirect URL from the POST data,
    # which indicates where to go after adding the item to the bag
    redirect_url = request.POST.get("redirect_url")

    # Get the current shopping bag from the session,
    # or initialize an empty dictionary if it doesn't exist
    bag = request.session.get("bag", {})

    # Check if the item is already in the bag
    if item_id in list(bag.keys()):
        # If it is, display a message indicating so
        messages.info(request, f"{game.title} is already in your bag.")
    else:
        # If it's not, add it with the specified quantity
        bag[item_id] = quantity
        # Success message indicating the item has been added to the bag
        messages.success(request, f"Added {game.title} to your bag")

    # Update the session's bag with the modified bag
    request.session["bag"] = bag

    # Redirect the user to the URL specified in the redirect_url
    return redirect(redirect_url)

def remove_from_bag(request, item_id):
    """
    This function removes an item from the shopping bag stored in the session.

    """

    try:
        game = get_object_or_404(Game, pk=item_id)
        bag = request.session.get("bag", {})
        bag.pop(item_id, None)  # Remove the item from the bag by its ID
        messages.success(request, f"Removed {game.title} from your bag")

        request.session["bag"] = bag

        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
