from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    Configuration class for the checkout app.

    This class defines configuration settings for the checkout app,
    including specifying the default type of auto field for primary keys
    and ensuring that signal handlers are connected
    when the application is ready.
    """
    # Specify the default type of auto field to be used for primary keys
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        """
        Override the ready method to import signals module.
        This ensures that the signal handlers are connected when
        the application is ready.
        """
        import checkout.signals
