from django.shortcuts import render, get_object_or_404
from .models import Game

# Create your views here.


def games_list(request):
    """A view to show all products, including sorting and search queries"""
    games = Game.objects.all()  # Fetch all games from the database
    # 'games' is the name of the variable that holds
    # the data you retrieve from the database
    # in your view function
    context = {
        "games_list": games,  # 'games_list' is the name of the key in the
                              # dictionary (context) that you pass to the 
                              # template. The template uses this key  
    }
    return render(request, "marketplace/games_list.html", context)


def game_detail(request, game_id):
    """A view to show individual product details"""
    game = get_object_or_404(Game, id=game_id)  # primary key lookup
    context = {
        "game": game,  

    }
    return render(request, "marketplace/game_detail.html", context)
