from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import FeedbackRequest


# Create your views here.

def index(request):
    """A view to return the index page"""

    return render(request, "home/index.html")


def about_page(request):
    """
    Render the About page.

    Retrieves the latest About page content and renders it along with
    the collaboration form.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered About page template.
    """
    if request.method == "POST":
        feedback_request = FeedbackRequest(data=request.POST)
        if feedback_request.is_valid():
            feedback_request.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Feedback received!",
            )

    about_page = About.objects.all().order_by("-updated_on").first()
    feedback_request = FeedbackRequest()

    return render(
        request,
        "home/about_page.html",
        {"about_page": about_page, "feedback_request": feedback_request},
    )
