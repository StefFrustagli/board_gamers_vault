from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderLineItem
from marketplace.models import Game
from profiles.models import UserProfile

import stripe
import json
import time


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """
        Send a confirmation email to the customer
        after successful order placement.

        Args:
            order (Order): The Order instance
            for which the email is being sent.
        """
        cust_email = order.email
        subject = render_to_string(
            "checkout/confirmation_emails/confirmation_email_subject.txt",
            {"order": order},
        )

        body = render_to_string(
            "checkout/confirmation_emails/confirmation_email_body.txt",
            {"order": order, "contact_email": settings.DEFAULT_FROM_EMAIL},
        )

        send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [cust_email])

    def notify_seller(self, order_line_item):
        """
        Notify the seller that their game has been sold and can be dispatched.

        Args:
            order_line_item (OrderLineItem):
            The OrderLineItem instance representing the sold game.
        """
        order_line_item.game.is_avalable = False
        order_line_item.game.save()
        seller = order_line_item.game.seller
        seller_email = seller.email

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

        # Send the email
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [seller_email],
            fail_silently=False,
        )

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event.

        Args:
            event (dict): The Stripe webhook event data.

        Returns:
            HttpResponse: HTTP response indicating successful
            receipt of the webhook event.
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}', status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe.

        This method processes successful payment intents,
        updates order information, notifies sellers,
        and sends confirmation emails.

        Args:
            event (dict): The Stripe webhook event data.

        Returns:
            HttpResponse: HTTP response indicating successful processing
            of the webhook event.
        """
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(intent.latest_charge)

        billing_details = stripe_charge.billing_details
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2)

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        if username != "AnonymousUser":
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number = shipping_details.phone
                profile.default_country = shipping_details.address.country
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_town_or_city = shipping_details.address.city
                profile.default_street_address1 = (
                    shipping_details.address.line1
                )
                profile.default_street_address2 = (
                    shipping_details.address.line2
                )
                profile.default_county = shipping_details.address.state
                profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
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
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if order_exists:
            # Notify sellers if the order already exists
            for lineitem in order.lineitems.all():
                self.notify_seller(lineitem)

            # Notify buyers
            self._send_confirmation_email(order)
            return HttpResponse(
                content=(
                    f'Webhook received: {event["type"]} '
                    '| SUCCESS: Verified order already in database'
                ),
                status=200,
            )
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    user_profile=profile,
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
                )
                for item_id, item_data in json.loads(bag).items():
                    game = Game.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            game=game,
                            quantity=item_data,
                        )
                        order_line_item.save()
                        # Notify the seller for each newly created line item
                        self.notify_seller(order_line_item)

            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500,
                )
        self._send_confirmation_email(order)
        return HttpResponse(
            content=(
                f'Webhook received: {event["type"]} '
                '| SUCCESS: Created order in webhook'
            ),
            status=200,
        )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe.

        Args:
            event (dict): The Stripe webhook event data.

        Returns:
            HttpResponse: HTTP response indicating receipt of webhook event.
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}', status=200)
