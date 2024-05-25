from django.contrib import admin
from .models import Game
from .models import Category

# Register your models here.

class GameAdmin(admin.ModelAdmin):
    list_display = (
        "listing_id",
        "title",
        "price",
        "condition",
        "category",
        "image",
        "seller",
        "description",
        "seller_comment",
    )

    ordering = ('listing_id',)

class CategoryAdmin(admin.ModelAdmin):   
    list_display = (
        'name',
    ) 
    
admin.site.register(Game, GameAdmin)
admin.site.register(Category, CategoryAdmin)
