from django import forms
from .models import *

class CreatePostForm(forms.ModelForm):
    class Meta:
        '''Associate form to model'''
        model = Post
        fields = ['caption']