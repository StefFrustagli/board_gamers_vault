import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from django_countries.fields import CountryField
from marketplace.models import Game
from profiles.models import UserProfile

# Create your models here.


class Order(models.Model):
    """
    A model representing an order in the system.

    This model captures details of an order placed by a user, including
    personal information, delivery address, and order specifics such as
    total cost and payment details.
    """

    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(
        UserProfile,
        # on_delete=models.CASCADE,
        on_delete=models.SET_NULL,
        null=True, blank=True, related_name='orders_linked'
    )
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label="Country *", null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    # Date and time when the order was created
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0
    )
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    original_bag = models.TextField(null=False, blank=False, default="")
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default=""
    )

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID.

        Returns:
            str: A unique order number in hexadecimal format.
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.

        The method recalculates the order total by summing up
        all line item totals. It then sets the delivery cost to zero
        and updates the grand total.
        """
        self.order_total = (
            self.lineitems.aggregate(Sum("lineitem_total"))[
                "lineitem_total__sum"
            ] or 0
        )

        # Set delivery cost to zero
        self.delivery_cost = 0

        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        """
        String representation of the order.

        Returns:
            str: The order number.
        """
        return self.order_number


class OrderLineItem(models.Model):
    """
    A model representing an individual line item in an order.

    This model captures details of a specific game ordered, including
    the quantity and calculated total price for that line item.
    """

    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="lineitems",
    )
    game = models.ForeignKey(
        Game,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )

    # Quantity 1
    quantity = models.PositiveIntegerField(default=1)

    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False
    )

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        self.lineitem_total = self.game.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        """
        String representation of the line item.

        Returns:
            str: A formatted string with the SKU and order number.
        """
        return f"SKU {self.game.sku} on order {self.order.order_number}"
