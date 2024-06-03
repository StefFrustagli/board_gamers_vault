from django.contrib import admin
from .models import Category, Game, SellerProfile
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

@admin.register(Game)
class GameAdmin(SummernoteModelAdmin):

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
    list_display = (
        "name",
        )


@admin.register(SellerProfile)
class SellerProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "standard_delivery_fee",
        "free_delivery_threshold",
    )
    search_fields = ["user__username"]
    list_filter = ("standard_delivery_fee", "free_delivery_threshold")
    list_editable = ("standard_delivery_fee", "free_delivery_threshold")
