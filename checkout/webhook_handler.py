from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.db import transaction

from .models import Order, OrderLineItem
from marketplace.models import Game
from profiles.models import UserProfile

import stripe
import json
import time


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        """
        Initialize the handler with the incoming request.
        The request contains Stripe webhook event data.
        """
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event.
        Args:
            event (dict): The Stripe webhook event data.
        """
        # Return a generic response to acknowledge receipt of the event
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200
        )

    def _send_confirmation_email(self, order):
        """
        Send a confirmation email to the customer
        after successful order placement.
        This method attempts to send the email
        and logs any errors encountered.

        Args:
            order (Order):
            The Order instance for which the email is being sent.
        """
        try:
            cust_email = order.email  # Get customer's email from order

            # Debugging: Print out the customer's email
            print(f"Customer Email: {cust_email}")
            # Render the email subject and body
            # using templates and order context
            subject = render_to_string(
                "checkout/confirmation_emails/confirmation_email_subject.txt",
                {"order": order},
            )
            body = render_to_string(
                "checkout/confirmation_emails/confirmation_email_body.txt",
                {"order": order, "contact_email": settings.DEFAULT_FROM_EMAIL},
            )

            # Send the email using Django's send_mail function.
            send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [cust_email])
        except Exception as e:
            # Log the error for debugging if sending email fails.
            print(f"Failed to send confirmation email: {e}")

    def notify_seller(self, order_line_item):
        """
        Notify the seller that their game has been sold and can be dispatched.

        Args:
            order_line_item (OrderLineItem):
            The line item representing the sold game.
        """
        # Mark the game as unavailable after it has been sold.
        order_line_item.game.is_avalable = False
        order_line_item.game.save()

        # Get the seller associated with the game.
        seller = order_line_item.game.seller
        seller_email = seller.email  # Retrieve the seller's email.

        # Render the email subject and body for notifying the seller.
        subject = render_to_string(
            "checkout/confirmation_emails/order_sold_email_subject.txt",
            {"order": order_line_item.order},
        )
        body = render_to_string(
            "checkout/confirmation_emails/order_sold_email_body.txt",
            {
                "order": order_line_item.order,
                "contact_email": settings.DEFAULT_FROM_EMAIL,
            },
        )

        try:
            # Send the email notification to the seller.
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [seller_email]
            )
        except Exception as e:
            # Log the error if sending the seller notification fails.
            print(f"Failed to notify seller: {e}")

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe,
        each time a user completes the payment process.
        This method processes successful payment intents,
        checks for existing orders,
        creates new orders if necessary,
        and sends emails to customers and sellers.

        Args:
            event (dict): The Stripe webhook event data.
        """
        # Extract payment intent object from event data.
        intent = event.data.object
        # print statement to log the intent for debugging
        print(intent)

        pid = intent.id  # Get the Stripe Payment Intent ID.
        # Retrieve the shopping bag data from the metadata.
        bag = intent.metadata.bag
        save_info = (
            intent.metadata.save_info
        )  # Check if the user wants to save their info.

        # Retrieve payment and shipping details
        stripe_charge = stripe.Charge.retrieve(intent.latest_charge)
        billing_details = (
            stripe_charge.billing_details
        )  # Billing details from the charge.
        shipping_details = intent.shipping  # Details from payment intent.
        grand_total = round(
            stripe_charge.amount / 100, 2
        )  # Calculate grand total from the charge amount.

        # Clean any empty fields in the shipping address to avoid null issues
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # If the user is authenticated (not anonymous),
        # update their profile with saved info.
        profile = None
        username = intent.metadata.username
        if username != "AnonymousUser":
            # Retrieve the user's profile using the username.
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                # Save the shipping details as default for the user's profile.
                profile.default_phone_number = shipping_details.phone
                profile.default_country = shipping_details.address.country
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_town_or_city = shipping_details.address.city
                profile.default_street_address1 = \
                    shipping_details.address.line1
                profile.default_street_address2 = \
                    shipping_details.address.line2
                profile.default_county = shipping_details.address.state
                profile.save()  # Save the updated profile.

        # Check if the order already exists in the database. Prevent duplicates
        order_exists = False
        order = None
        try:
            # Try to find an order with the matching payment & shipping details
            order = Order.objects.get(
                full_name__iexact=shipping_details.name,
                email__iexact=billing_details.email,
                phone_number__iexact=shipping_details.phone,
                country__iexact=shipping_details.address.country,
                postcode__iexact=shipping_details.address.postal_code,
                town_or_city__iexact=shipping_details.address.city,
                street_address1__iexact=shipping_details.address.line1,
                street_address2__iexact=shipping_details.address.line2,
                county__iexact=shipping_details.address.state,
                grand_total=grand_total,
                original_bag=bag,
                stripe_pid=pid,
            )
            order_exists = True  # Mark that the order already exists.
        except Order.DoesNotExist:
            # If the order does not exist, we'll create a new one.
            pass

        # If the order already exists, send the necessary notifications
        if order_exists:
            # Notify each seller associated with the order line items.
            for lineitem in order.lineitems.all():
                self.notify_seller(lineitem)
            # Send confirmation email to the customer.
            self._send_confirmation_email(order)
            return HttpResponse(
                content=(
                    f'Webhook received: {event["type"]} | '
                    f"SUCCESS: Verified order already in database"
                ),
                status=200,
            )

        # If the order does not exist, proceed to create a new one.
        try:
            # Start a transaction to ensure order creation is atomic.
            with transaction.atomic():
                # Create a new Order object with the shipping & payment details
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    user_profile=profile,  # Set user profile if available.
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_bag=bag,
                    stripe_pid=pid,
                    grand_total=grand_total,
                )

                # Loop through each item in the bag to create order line items
                for item_id, item_data in json.loads(bag).items():
                    game = Game.objects.get(id=item_id)
                    if isinstance(item_data, int):  # quantity is integer
                        # Create new OrderLineItem for each game in the order
                        order_line_item = OrderLineItem(
                            order=order,
                            game=game,
                            quantity=item_data,
                        )
                        order_line_item.save()
                        # Notify the seller about the sale of this game.
                        self.notify_seller(order_line_item)

            # After successfully creating the order,
            # send a confirmation email to the customer.
            self._send_confirmation_email(order)
            # Return a success response to Stripe, including the event type
            return HttpResponse(
                content=(
                    f'Webhook received: {event["type"]} | '
                    f"SUCCESS: Created order in webhook"
                ),
                status=200,
            )

        except Exception as e:
            # If an error occurs during order creation,
            # delete the order and return an error response.
            if order:
                order.delete()
            # print statement for logging the error
            print(f"Error occurred: {e}")
            return HttpResponse(
                content=(
                    f'Webhook received: {event["type"]} | '
                    f"ERROR: {e}"
                ),
                status=500,
            )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
