from django.urls import path, include
from . import views

# URL pattern for listing games
urlpatterns = [
    path("", views.games_list, name="games_list"),
    path("<int:game_id>/", views.game_detail, name="game_detail"),
    path("add/", views.add_game, name="add_game"),
]
