from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    Form for creating and updating user profiles.

    This form extends the Django ModelForm to customize fields and
    widgets for the UserProfile model. It excludes the 'user' field
    since it's automatically set based on the logged-in user.

    Attributes:
        Meta: Metadata class to specify the model and excluded fields.
    """
    class Meta:
        model = UserProfile
        exclude = ("user",)

    def __init__(self, *args, **kwargs):
        """
        Initialize the form with placeholders, classes, and other
        field attributes. Removes auto-generated labels and sets
        autofocus on the first field.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            "user": "User",
            "avatar": "Avatar",
            "default_town_or_city": "Town or city",
            "bio": "About me",
            "games_for_sale": "Board Games I want to sell",
            "games_owned": "My collection",
        }

        self.fields["default_town_or_city"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if field != "default_town_or_city":
                if self.fields[field].required:
                    placeholder = f"{placeholders[field]} *"
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].widget.attrs[
                "class"
            ] = "border-black rounded-0 profile-form-input"
            self.fields[field].label = False
