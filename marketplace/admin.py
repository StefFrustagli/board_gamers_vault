from django.contrib import admin
from .models import Category, Game, SellerProfile
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

@admin.register(Game)
class GameAdmin(SummernoteModelAdmin):
    """
    Admin interface options for the Game model.

    Provides the ability to display, search, filter,
    and edit fields for the Game model.
    """

    list_display = (
        "sku",
        "title",
        "price",
        "condition",
        "category",
        "image",
        "seller",
        "description",
        "seller_comment",
    )
    search_fields = ["title"]
    list_filter = ("seller",)
    prepopulated_fields = {"sku": ("title",)}
    summernote_fields = ("description")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin interface options for the Category model.

    Provides the ability to display fields for the Category model.
    """
    list_display = (
        "name",
        )


@admin.register(SellerProfile)
class SellerProfileAdmin(admin.ModelAdmin):
    """
    Admin interface options for the SellerProfile model.

    Provides the ability to display, search, filter, and edit fields
    for the SellerProfile model.
    """
    list_display = (
        "user",
        "standard_delivery_fee",
        "free_delivery_threshold",
    )
    search_fields = ["user__username"]
    list_filter = ("standard_delivery_fee", "free_delivery_threshold")
    list_editable = ("standard_delivery_fee", "free_delivery_threshold")
