from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


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


class Game(models.Model):
    CONDITION_CHOICES = [
        ("as_new", "As new"),
        ("great", "Great"),
        ("good", "Good"),
        ("fair", "Fair"),
        ("signs_of_times", "Signs of times"),
        ("heavily_used", "Heavily used"),
    ]

    listing_id = models.CharField(max_length=100, unique=True, blank=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    condition = models.CharField(max_length=15, choices=CONDITION_CHOICES)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name="games"
    )
    image = models.ImageField(upload_to="game_images/")
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="games"
    )
    description = models.TextField()
    seller_comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
