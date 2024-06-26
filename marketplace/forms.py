from django import forms
from .widgets import CustomClearableFileInput
from .models import Game, Category


class GameForm(forms.ModelForm):
    """
    Form for creating and updating Game instances.
    """

    class Meta:
        model = Game
        # fields = "__all__"  # Use all fields from the Game model
        exclude = ["seller"]

    image = forms.ImageField(
        label="Image", required=False, widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        """
        Initialize the form and dynamically populate category choices.
        Add CSS classes to form fields for consistent styling.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)

        # Retrieve all categories from the database
        categories = Category.objects.all()

        # Create a list of tuples with category id and name
        name = [(c.id, c.name) for c in categories]

        # Set the category field choices to the retrieved categories
        self.fields["category"].choices = name

        self.fields["price"].label = "Price (£)"

        # Add CSS classes to form fields for styling
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-black rounded-0"
