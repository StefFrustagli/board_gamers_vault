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

    # Add categories to the database
    # Category.objects.bulk_create(
    #     [
    #         Category(name="Role-playing"),
    #         Category(name="Cooperatives"),
    #         Category(name="Bluffing"),
    #         Category(name="Area control"),
    #         Category(name="Placement"),
    #         Category(name="Memory"),
    #         Category(name="Miniatures"),
    #         Category(name="War games"),
    #         Category(name="Worker placement"),
    #         Category(name="Strategy"),
    #         Category(name="Deck Building"),
    #         Category(name="City Building"),
    #         Category(name="Party Games"),
    #         Category(name="Storytelling"),
    #     ]
    # )

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

    sku = models.CharField(max_length=12, unique=True, blank=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    condition = models.CharField(max_length=15, choices=CONDITION_CHOICES)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name="games"
    )
    image = models.ImageField(upload_to="game_images/")
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="games")
    description = models.TextField()
    seller_comment = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = self.generate_sku()
        super(Game, self).save(*args, **kwargs)

    def generate_sku(self):
        return get_random_string(length=12)

    def __str__(self):
        return self.title
