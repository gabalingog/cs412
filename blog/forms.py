# forms to update and create and delete

from django import forms
from .models import Article

# create a form class

class CreateArticleForm(forms.ModelForm):
    class Meta:
        '''Associate form to model'''
        model = Article
        fields = ['author', 'title', 'text', 'image_url']
        