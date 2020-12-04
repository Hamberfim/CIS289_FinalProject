"""Defines the urls patterns for the users app"""
from django.urls import path
from django.urls import include


app_name = 'users'
urlpatterns = [
    # default authorization url for django's default login view
    path('', include('django.contrib.auth.urls')),

]
