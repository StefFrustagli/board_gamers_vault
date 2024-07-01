from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from marketplace.models import Game, SellerProfile


class UserProfile(models.Model):
    """
    A user profile model for maintaining public information
    like games for sale, games owned, bio, avatar and city,
    as well as private information like order history.

    Attributes:
        user (User): One-to-one relationship with the User model.
        avatar (ImageField): Profile picture of the user.
        default_town_or_city (CharField): Default city or town of the user.
        bio (TextField): Biography or about me section of the user.
        games_for_sale (ManyToManyField): Games listed for sale by the user.
        games_owned (ManyToManyField): Games owned by the user.

    Methods:
        __str__: Returns the username of the associated User instance.
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    default_town_or_city = models.CharField(
        max_length=25,
        null=True,
        blank=True
    )
    bio = models.TextField(null=True, blank=True)
    games_for_sale = models.ManyToManyField(
        Game, related_name="games_for_sale_by_user", blank=True
    )
    games_owned = models.ManyToManyField(
        Game, related_name="games_owned_by_user", blank=True
    )
    # orders = models.ManyToManyField(
    #     "checkout.Order", related_name="user_orders", blank=True
    # )

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Signal handler to create or update the UserProfile
    when a User instance is saved.

    Args:
        sender: The model class that sends the signal (User).
        instance: The actual instance being saved (User instance).
        created (bool): True if a new instance was created,
        False if it was updated.

    Returns:
        None
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
