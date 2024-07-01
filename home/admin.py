from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import About, FeedbackRequest


# Register your models here.
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the About model using Summernote.

    This class extends SummernoteModelAdmin to enable rich text editing
    for the 'content' field of the About model.

    Attributes:
        summernote_fields (tuple): Fields to enable Summernote
        for rich text editing.
    """
    summernote_fields = ("content",)

@admin.register(FeedbackRequest)
class FeedbackRequestAdmin(admin.ModelAdmin):
    """
    Admin configuration for the FeedbackRequest model.

    This class configures the display of FeedbackRequest instances
    in the Django admin interface.

    Attributes:
        list_display (tuple): Fields to display in the list view
        of the admin interface.
    """
    list_display = (
        "message",
        "read",
    )
