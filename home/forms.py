from .models import FeedbackRequest
from django import forms


class FeedbackRequest(forms.ModelForm):
    """
    Form for handling feedback requests.

    This form is used to collect feedback request information from users,
    including their name, email address, and message.

    Attributes:
        Meta (inner class): Specifies the model and fields for the form.

    Example:
        To use this form in a Django view:

        ```python
        from django.shortcuts import render
        from .forms import FeedbackRequestForm

        def feedback_view(request):
            if request.method == 'POST':
                form = FeedbackRequestForm(request.POST)
                if form.is_valid():
                    form.save()
                    # Handle successful form submission
            else:
                form = FeedbackRequestForm()

            return render(request, 'feedback_template.html', {'form': form})
        ```
    """
    class Meta:
        model = FeedbackRequest
        fields = ("name", "email", "message")
