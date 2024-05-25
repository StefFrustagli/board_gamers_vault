from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Game(models.Model):
    CONDITION_CHOICES = [
        ("as_new", "As new"),
        ("great", "Great"),
        ("good", "Good"),
        ("fair", "Fair"),
        ("signs_of_times", "Signs of times"),
        ("heavily_used", "Heavily used"),
    ]

    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    condition = models.CharField(max_length=15, choices=CONDITION_CHOICES)
    image = models.ImageField(upload_to="game_images/")
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="games"
    )
    description = models.TextField()
    seller_comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


