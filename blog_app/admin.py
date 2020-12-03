from django.contrib import admin
# import the class models from models.py and register them
from .models import Topic

# Register your models here.
admin.site.register(Topic)
