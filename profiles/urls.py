from django.urls import path
from . import views

urlpatterns = [
    path("profile/", views.profile, name="profile"),
    path(
        "order_history/<order_number>",
        views.order_history,
        name="order_history"
    ),
]

"""
URL patterns for the profiles app.

Includes paths for:
- profile: View user profile details.
- order_history/<order_number>:
View order history details for a specific order.

These patterns define the endpoints accessible within the profiles app.
"""
