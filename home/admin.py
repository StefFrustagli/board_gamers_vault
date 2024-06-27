from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import About, FeedbackRequest


# Register your models here.
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ("content",)

@admin.register(FeedbackRequest)
class FeedbackRequestAdmin(admin.ModelAdmin):

    list_display = (
        "message",
        "read",
    )
