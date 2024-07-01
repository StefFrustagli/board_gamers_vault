from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from marketplace.models import Game, SellerProfile


def bag_contents(request):
    """
    Calculate and return the contents of the shopping bag, including the
    items, total cost, product count, and delivery cost.

    This function performs the following operations:
    1. Initializes variables to store bag items, total cost, product count,
       and delivery cost.
    2. Retrieves the shopping bag from the session.
    3. Iterates through the items in the bag to:
       a. Fetch each game from the database using its ID.
       b. Calculate the total cost for each item and update the total cost.
       c. Increment the product count.
       d. Check if the seller has a seller_profile
        and handle cases where they do not.
       e. Add the item details to the bag_items list.
    4. Calculate the grand total including delivery cost.
    5. Return the context dictionary containing bag details.

    Args:
        request: The HTTP request object containing session data.

    Returns:
        A dictionary with the following keys:
        - bag_items: List of items in the bag.
        - total: Total cost of items in the bag.
        - product_count: Total number of products in the bag.
        - delivery: Total delivery cost (currently set to 0).
        - free_delivery_delta: Amount remaining to qualify for free delivery.
        - free_delivery_threshold: The threshold cost for free delivery.
        - grand_total: The grand total cost including delivery.
    """
    # Initialize variables to store bag items,
    # total cost, product count, and delivery cost
    bag_items = []
    total = 0
    product_count = 0
    # Delivery will be included in the product price
    delivery = 0

    # Get the shopping bag from the session
    bag = request.session.get("bag", {})

    # Iterate through items in the bag
    for item_id, quantity in bag.items():
        # Fetch the game from the database using its ID
        game = get_object_or_404(Game, pk=item_id)
        # Calculate the total cost for the item and add to the total
        total += quantity * game.price
        # Increment the product count
        product_count += quantity
        # Get the seller of the game
        seller = game.seller

        # Check if the seller has a seller_profile
        if hasattr(seller, "seller_profile"):
            seller_profile = seller.seller_profile
        else:
            # Handle the case where the seller does not have a seller_profile
            # For example, set a default value or log an error
            seller_profile = None
            print(f"Seller {seller.id} does not have a seller_profile.")

        # Add the item details to the bag_items list
        bag_items.append(
            {
                "item_id": item_id,
                "quantity": quantity,
                "game": game,
            }
        )

    # Calculate the grand total including delivery
    grand_total = total

    context = {
        "bag_items": bag_items,
        "total": total,
        "product_count": product_count,
        "delivery": delivery,
        "free_delivery_delta":
            max(settings.FREE_DELIVERY_THRESHOLD - total, 0),
        "free_delivery_threshold": settings.FREE_DELIVERY_THRESHOLD,
        "grand_total": grand_total,
    }

    return context
