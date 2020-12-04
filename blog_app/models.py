from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
# This model tells Django how to work with the data that will be stored in the app
class Topic(models.Model):
    """A topic the admin user enters.
    This class inherits from the 'Model' parent class that's included in Django.
    """
    text = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Entry(models.Model):
    """A specific blog entry related to an existing topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    # text = models.TextField()
    text = RichTextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'  # correct display so it doesn't show up as 'entrys'

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.text[:50]}..."
