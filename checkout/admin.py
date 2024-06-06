from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Inline admin interface for order line items. This allows line items to be 
    edited within the Order admin interface.
    """
    model = OrderLineItem
    readonly_fields = ("lineitem_total",)  # lineitem_total field read-only


class OrderAdmin(admin.ModelAdmin):
    """
    Admin interface for Orders. This configures how the Order model is displayed
    and managed within the Django admin interface.
    """
    # Include the OrderLineItem inline admin
    inlines = (OrderLineItemAdminInline,)  

    readonly_fields = (
        "order_number",
        "date",
        "delivery_cost",
        "order_total",
        "grand_total",
    )  # Make certain fields read-only

    # Fields to be displayed in the admin form
    fields = (
        "order_number",
        "date",
        "full_name",
        "email",
        "phone_number",
        "country",
        "postcode",
        "town_or_city",
        "street_address1",
        "street_address2",
        "county",
        "delivery_cost",
        "order_total",
        "grand_total",
    )

    # Fields to be displayed in the admin list view
    list_display = (
        "order_number",
        "date",
        "full_name",
        "order_total",
        "delivery_cost",
        "grand_total",
    )
    # Default ordering to be by date, descending
    ordering = ("-date",)

# Register the Order model with the OrderAdmin configuration
admin.site.register(Order, OrderAdmin)
