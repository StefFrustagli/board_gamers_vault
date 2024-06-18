from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from marketplace.models import Game, SellerProfile

def bag_contents(request):
    # Initialize variables to store bag items,
    # total cost, product count, and delivery cost
    bag_items = []
    total = 0
    product_count = 0
    delivery = 0

    # Dictionary to keep track of delivery charges for each seller
    seller_delivery_charges = {}

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

        # Check if the seller's delivery charge is already calculated
        if seller.id not in seller_delivery_charges:
            # Calculate delivery charge if the total is below the free delivery threshold
            if total < settings.FREE_DELIVERY_THRESHOLD:
                seller_delivery_charges[seller.id] = (
                    seller_profile.standard_delivery_fee if seller_profile else 0
                )
            else:
                seller_delivery_charges[seller.id] = 0
                
        # Add the item details to the bag_items list
        bag_items.append(
            {
                "item_id": item_id,
                "quantity": quantity,
                "game": game,
            }
        )

    # Sum up the delivery charges from all sellers
    for charge in seller_delivery_charges.values():
        delivery += charge

    # Calculate the grand total including delivery
    grand_total = delivery + total

    context = {
        "bag_items": bag_items,
        "total": total,
        "product_count": product_count,
        "delivery": delivery,
        "free_delivery_delta": max(settings.FREE_DELIVERY_THRESHOLD - total, 0),
        "free_delivery_threshold": settings.FREE_DELIVERY_THRESHOLD,
        "grand_total": grand_total,
    }

    return context
