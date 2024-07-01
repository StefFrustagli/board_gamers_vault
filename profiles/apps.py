from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
    AppConfig for the 'profiles' Django application.

    This class defines configuration settings for the 'profiles' app,
    specifying the default auto-generated field and the name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
