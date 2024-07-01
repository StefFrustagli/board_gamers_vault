from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    A form for creating and updating Order instances. This form
    includes fields for the user's personal information and address details.
    """

    class Meta:
        model = Order
        fields = (
            "full_name",
            "email",
            "phone_number",
            "street_address1",
            "street_address2",
            "town_or_city",
            "postcode",
            "country",
            "county",
        )

    def __init__(self, *args, **kwargs):
        """
        Customize the form initialization to add placeholders and CSS classes,
        remove auto-generated labels, and set autofocus on the first field.
        """
        super().__init__(*args, **kwargs)

        # Define placeholders for each form field
        placeholders = {
            "full_name": "Full Name",
            "email": "Email Address",
            "phone_number": "Phone Number",
            "postcode": "Postal Code",
            "town_or_city": "Town or City",
            "street_address1": "Street Address 1",
            "street_address2": "Street Address 2",
            "county": "County, State or Locality",
        }

        # Set autofocus on the full_name field
        self.fields["full_name"].widget.attrs["autofocus"] = True

        # Iterate over all form fields to add custom attributes
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f"{placeholders[field]} *"
                else:
                    placeholder = placeholders[field]
                # Add placeholder text and CSS class to each field's widget
                self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].widget.attrs["class"] = "stripe-style-input"
            # Remove the default label for each field
            self.fields[field].label = False
