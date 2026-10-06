# forms to update and create and delete

from django import forms
from .models import Article, Comment

# create a form class

class CreateArticleForm(forms.ModelForm):
    class Meta:
        '''Associate form to model'''
        model = Article
        # fields = ['author', 'title', 'text', 'image_url']
        fields = ['author', 'title', 'text', 'image_file']
        
# form to create comments
class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']