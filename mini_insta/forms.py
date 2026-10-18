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

class UpdateProfileForm(forms.ModelForm):
    '''Update the profile of users'''
    class Meta:
        model = Profile
        fields = ['display_name', 'profile_image_url', 'bio_text']

class UpdatePostForm(forms.ModelForm):
    '''Updates a post from a user'''
    class Meta:
        model = Post
        fields = ['caption']