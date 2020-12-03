from django.db import models


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
