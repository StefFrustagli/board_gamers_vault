from django.apps import AppConfig


class HomeConfig(AppConfig):
    """
    AppConfig for the 'home' Django application.

    This AppConfig defines the configuration for the 'home' app,
    including the default auto field setting and the app name.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

class AboutPageConfig(AppConfig):
    """
    AppConfig for the 'about_page' Django application.

    This AppConfig defines the configuration for the 'about_page' app,
    including the default auto field setting and the app name.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'about_page'
