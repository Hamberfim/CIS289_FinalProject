"""Defines urls pattern for dj_blog_app."""
from django.urls import path
from . import views


app_name = 'blog_app'
urlpatterns = [
    # home/index page
    path('', views.index, name='index'),
    # show all topics
    path('topics/', views.topics, name='topics'),
    # public detail page of a topic
    path('pub_topic/<int:topic_id>/', views.pub_topic, name='pub_topic'),
    # detail page of a topic
    path('topic/<int:topic_id>/', views.topic, name='topic'),
    # page for adding new topics by the users
    path('new_topic/', views.new_topic, name='new_topic'),
    # page for adding a new blog entry under a topic
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for editing a blog entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
