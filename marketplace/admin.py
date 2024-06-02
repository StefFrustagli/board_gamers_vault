from django.contrib import admin
from .models import Category, Game
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
