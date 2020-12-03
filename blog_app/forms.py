"""Topic Model Form"""
from django import forms
from .models import Topic
from .models import Entry


class TopicForm(forms.ModelForm):
    """Topic form - using Django ModelForm"""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}  # empty '' means don't generate a label for the text field


class EntryForm(forms.ModelForm):
    """Blog entry form - using Django ModelForm"""
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 79})}
