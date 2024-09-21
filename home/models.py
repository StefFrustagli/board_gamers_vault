from bs4 import BeautifulSoup
from django.db import models

# Create your models here.


# Function to clean HTML content (for Summernote)
def clean_html(content):
    soup = BeautifulSoup(content, "html.parser")
    for font_tag in soup.findAll("font"):
        font_tag.unwrap()  # Removes <font> tags but keeps the text
    return str(soup)


class About(models.Model):
    """
    Model representing the About page.

    Attributes:
        title (str): The title of the About page.
        updated_on (DateTime): The date and time when
        the About page was last updated.
        content (str): The content of the About page.
    """
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def save(self, *args, **kwargs):
        # Clean the content field before saving
        self.content = clean_html(self.content)
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the About page.

        Returns:
            str: The title of the About page.
        """
        return self.title


class FeedbackRequest(models.Model):
    """
    Model representing a feedback request.

    Attributes:
        name (str): The name of the person sending the message.
        email (str): The email address of the person sending the message.
        message (str): The text of the message.
        read (bool): A boolean indicating whether the message has been read.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        """
        Returns a string representation of the feedback/collaboration request.

        Returns:
            str: A formatted string indicating the source of the message.
        """
        return f"Feedback request from {self.name}"
