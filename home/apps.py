from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

class AboutPageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'about_page'
