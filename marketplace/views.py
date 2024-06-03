from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Game, Category

# Create your views here.


def games_list(request):
    """A view to show all products, including sorting and search queries"""
    games = Game.objects.all()  # Fetch all games from the database
    # 'games' is the name of the variable that holds
    # the data you retrieve from the database
    # in your view function
    query = None
    categories = None
    conditions = None
    sort = None
    direction = None   
    no_games_message = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'title': # should I change this into title instead?
                sortkey = 'lower_title'
                games = games.annotate(lower_name=Lower('title'))
            if sortkey == 'category':
                sortkey = 'category__name'     
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f"-{sortkey}"
            games = games.order_by(sortkey)        

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            games = games.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

            if not games.exists():
                no_games_message = "No games found for the selected category."  
                print(
                    "DEBUG: No games found for the selected category"
                )  # Debugging print statement

        if 'condition' in request.GET:
            conditions = request.GET['condition'].split(',')
            games = games.filter(condition__in=conditions)

            if not games.exists():
                no_games_message = "No games found for the selected condition."

        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "Please enter a search criteria.")
                return redirect(reverse("games_list"))

            queries = Q(title__icontains=query) | Q(description__icontains=query)
            # i makes the case insensitive
            games = games.filter(queries)

    current_sorting = f"{sort}_{direction}"

    context = {
        "games_list": games,  # 'games_list' is the name of the key in the
        # dictionary (context) that you pass to the
        # template. The template uses this key
        "search_term": query,
        "current_categories": categories,
        "current_conditions": conditions,
        "current_sorting": current_sorting,
        "no_games_message": no_games_message,
    }
    return render(request, "marketplace/games_list.html", context)


def game_detail(request, game_id):
    """A view to show individual product details"""
    game = get_object_or_404(Game, id=game_id)  # primary key lookup
    context = {
        "game": game,
    }
    return render(request, "marketplace/game_detail.html", context)
