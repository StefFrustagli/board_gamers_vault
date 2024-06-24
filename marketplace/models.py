from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

# Create your models here.


class Category(models.Model):
    CATEGORY_CHOICES = [
        ("role_playing", "Role-playing"),
        ("cooperatives", "Cooperatives"),
        ("bluffing", "Bluffing"),
        ("area_control", "Area control"),
        ("placement", "Placement"),
        ("memory", "Memory"),
        ("miniatures", "Miniatures"),
        ("war_games", "War games"),
        ("worker_placement", "Worker placement"),
        ("strategy", "Strategy"),
        ("deck_building", "Deck Building"),
        ("city_building", "City Building"),
        ("party_games", "Party Games"),
        ("storytelling", "Storytelling"),
    ]

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=100, choices=CATEGORY_CHOICES, unique=True)

    def __str__(self):
        return self.get_name_display()  # Display the human-readable value


class Game(models.Model):
    CONDITION_CHOICES = [
        ("as_new", "As new"),
        ("great", "Great"),
        ("good", "Good"),
        ("fair", "Fair"),
        ("signs_of_time", "Signs of time"),
        ("heavily_used", "Heavily used"),
    ]

    sku = models.CharField(max_length=40, unique=True, blank=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    condition = models.CharField(max_length=15, choices=CONDITION_CHOICES)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name="games"
    )
    image = models.ImageField(upload_to="game_images/", blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="games")
    description = models.TextField()
    seller_comment = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = self.generate_sku()
        super(Game, self).save(*args, **kwargs)

    def generate_sku(self):
        return get_random_string(length=40)

    def __str__(self):
        return self.title
    
    @property
    def availability_status(self):
        return "Available" if self.is_available else "Not Available"

    def mark_as_purchased(self):
        self.is_available = False
        self.save()


class SellerProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="seller_profile"
    )
    standard_delivery_fee = models.DecimalField(
        max_digits=10, decimal_places=2, default=5.00
    )
    free_delivery_threshold = models.DecimalField(
        max_digits=10, decimal_places=2, default=50.00
    )

    def __str__(self):
        return self.user.username
