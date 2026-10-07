# File: mini_insta/models.py
# Author: Gab Alingog (galingog@bu.edu), 10/07/2026
# Description: Needed for the creation form

from django import forms
from .models import *

class CreatePostForm(forms.ModelForm):
    class Meta:
        '''Associate form to model'''
        model = Post
        fields = ['caption']