from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from marketplace.models import Game


@login_required
def view_bag(request):
    """
    Render the bag contents page.

    This view requires the user to be logged in.
    It fetches the current contents of the shopping bag
    from the session and renders the 'bag/bag.html' template.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered bag contents page.
    """
    return render(request, "bag/bag.html")


@login_required
def add_to_bag(request, item_id):
    """
    Add a specified game to the shopping bag.

    This view requires the user to be logged in. It fetches the game using the
    provided item ID, checks if it is available, and adds it to the shopping
    bag stored in the session. If the game is already in the bag, it shows an
    informational message.

    Args:
        request: The HTTP request object containing session and POST data.
        item_id: The ID of the game to be added to the bag.

    Returns:
        HttpResponse: Redirects to the URL specified in the POST data or the
        marketplace page if the redirect URL is not specified.
    """
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
    redirect_url = request.POST.get("redirect_url", "/marketplace/")

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


@login_required
def remove_from_bag(request, item_id):
    """
    Remove a specified game from the shopping bag.
    This view requires the user to be logged in.
    It fetches the game using the provided item ID and removes
    it from the shopping bag stored in the session.
    If the removal is successful, it shows a success message.
    If an error occurs, it shows an error message.

    Args:
        request: The HTTP request object containing session data.
        item_id: The ID of the game to be removed from the bag.

    Returns:
        HttpResponse: An HTTP response with status 200
        if the removal is successful,
        or status 500 if an error occurs.
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
