from django.urls import path, include
from . import views

# URL pattern for listing games
urlpatterns = [
    path("", views.games_list, name="games_list"),
]
