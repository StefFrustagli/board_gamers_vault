from django.apps import AppConfig


class CheckoutConfig(AppConfig):
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
