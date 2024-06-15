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
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        default=None,
        null=True,  # Add null=True temporarily
    )
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    games_for_sale = models.ManyToManyField(
        Game, related_name="games_for_sale", blank=True
    )
    games_owned = models.ManyToManyField(Game, related_name="games_owned", blank=True)
    # orders = models.ManyToManyField(
    #     "checkout.Order", related_name="user_orders", blank=True
    # )

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
