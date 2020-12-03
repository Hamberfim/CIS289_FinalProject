from django.contrib import admin
# import the class models from models.py and register them
from .models import Topic
from .models import Entry

# Register your models here.
admin.site.register(Topic)
admin.site.register(Entry)
