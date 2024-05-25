from django.contrib import admin
from .models import Game
from .models import Category

# Register your models here.
admin.site.register(Game)
admin.site.register(Category)
