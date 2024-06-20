from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Game, Category
from .forms import GameForm

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
            if sortkey == 'title': 
                sortkey = 'lower_title'
                games = games.annotate(lower_title=Lower('title'))
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


def add_game(request):
    """Add a product to the store"""
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            game = form.save()  # Save the form data to a variable
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('game_detail', args=[game>id]))
        else:
            messages.error(request, 'Failed to add product. ' 
                                    'Please ensure the form is valid.')
    else:    
        form = GameForm()

    template = "marketplace/add_game.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


def edit_game(request, game_id):
    """Edit a product"""
    game = get_object_or_404(Game, pk=game_id)

    if request.method == "POST":
        form = GameForm(request.POST, request.FILES, instance=game)
        if form.is_valid():
            game = form.save()
            messages.success(request, "Product successfully updated!")
            return redirect(reverse("game_detail", args=[game.id]))
     # If form is invalid, continue to render the form with error messages
    else:
        form = GameForm(instance=game)
        messages.info(request, f"You are editing {game.title}")

    # This else block ensures that when the form is invalid during editing, the error message is set correctly
    if not form.is_valid() and request.method == "POST":
        messages.error(
            request, "Failed to update game. Please ensure the form is valid."
        )

    template = "marketplace/edit_game.html"
    context = {
        "form": form,
        "game": game,
    }

    return render(request, template, context)


def delete_game(request, game_id):
    """ Delete a product from the store """
    game = get_object_or_404(Game, pk=game_id)
    game.delete()
    messages.success(request, 'Game deleted!')
    return redirect(reverse('games'))
