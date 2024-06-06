from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Signal receiver for the post_save signal. This function updates the order total
    whenever an OrderLineItem instance is created or updated.

    Args:
        sender (Model): The model class that sent the signal.
        instance (OrderLineItem): The actual instance being saved.
        created (bool): A boolean; True if a new record was created.
        **kwargs: Additional keyword arguments.
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_save(sender, instance, **kwargs):
    """
    Signal receiver for the post_delete signal. This function updates the order total
    whenever an OrderLineItem instance is deleted.

    Args:
        sender (Model): The model class that sent the signal.
        instance (OrderLineItem): The actual instance being deleted.
        **kwargs: Additional keyword arguments.
    """
    instance.order.update_total()
