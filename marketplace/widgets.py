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
    clear_checkbox_label = _("Remove")
    initial_text = _("Current Image")
    input_text = _("")
    template_name = (
        "marketplace/custom_widget_templates/custom_clearable_file_input.html"
    )
