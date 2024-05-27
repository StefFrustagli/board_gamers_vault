from django.shortcuts import render
from .models import Game

# Create your views here.


def games_list(request):
    """A view to show all products, including sorting and search queries"""
    print("View function called")  # Debug print statement
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
