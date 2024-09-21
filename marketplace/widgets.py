from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    """
    A custom file input widget with clearable functionality.

    This widget extends Django's ClearableFileInput to provide custom
    labels and template for handling file inputs in forms. It allows
    users to clear the current file and upload a new one.

    Attributes:
        clear_checkbox_label (str): Label for the clear checkbox.
        initial_text (str): Text displayed for the initial file.
        input_text (str): Text displayed for the input field.
        template_name (str): Path to the custom template
        for rendering the widget.
    """
    initial_text = _("Here's your current image")
    input_text = _("Upload a new image:")
    template_name = (
        "marketplace/custom_widget_templates/custom_clearable_file_input.html"
    )

    # Override the method to remove the clear checkbox rendering
    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        # Remove the 'clear' related context variables
        context["widget"].pop("clear_checkbox_name", None)
        context["widget"].pop("clear_checkbox_id", None)
        context["widget"].pop("clear", None)
        return context
