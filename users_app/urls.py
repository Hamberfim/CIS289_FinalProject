"""Defines the urls patterns for the users control app"""
from django.urls import path
from django.urls import include
from . import views

app_name = 'users'
urlpatterns = [
    # default authorization url for django's default login view
    path('', include('django.contrib.auth.urls')),
    # registration page
    path('register/', views.register, name='register'),

]
