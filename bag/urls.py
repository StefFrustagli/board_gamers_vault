from django.urls import path
from . import views

urlpatterns = [
    # URL pattern for viewing the bag.
    # This pattern matches the root URL of the bag app
    # and maps it to the view_bag view.
    # 'view_bag' can be used to refer to this URL pattern in templates and views.
    path("", views.view_bag, name="view_bag"),
    # URL pattern for adding an item to the bag.
    # This pattern matches URLs of the form "add/<item_id>/"
    # where <item_id> is a placeholder for the ID of the item being added.
    # The item_id is passed as an argument to the add_to_bag view.
    # The name 'add_to_bag' can be used to refer to this URL pattern
    # in templates and views.
    path("add/<item_id>/", views.add_to_bag, name="add_to_bag"),
    path("remove/<item_id>/", views.remove_from_bag, name="remove_from_bag"),
]
