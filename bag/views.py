from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def view_bag(request):
    """A view that renders the bag contents page"""

    return render(request, "bag/bag.html")


def add_to_bag(request, item_id):
    """Add a quantity of the specified product to the shopping bag"""

    # Quantity always one as unique item
    quantity = 1

    # Retrieve the redirect URL from the POST data,
    # which indicates where to go after adding the item to the bag
    redirect_url = request.POST.get("redirect_url")

    # Get the current shopping bag from the session,
    # or initialize an empty dictionary if it doesn't exist
    bag = request.session.get("bag", {})

    # Check if the item is already in the bag
    if item_id in list(bag.keys()):
        # If it is, increment the quantity by the amount specified
        bag[item_id] += quantity
        # If it's not, add it with the specified quantity
    else:
        bag[item_id] = quantity

    # Update the session's bag with the modified bag
    request.session["bag"] = bag

    # Redirect the user to the URL specified in the redirect_url
    return redirect(redirect_url)

def remove_from_bag(request, item_id):
    """
    Remove the item from the shopping bag.

    This function removes an item from the shopping bag stored in the session.
    """

    try:
        bag = request.session.get("bag", {})
        bag.pop(item_id, None)  # Remove the item from the bag by its ID

        request.session["bag"] = bag
        
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
