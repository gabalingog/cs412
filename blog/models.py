from django.db import models
from django.urls import reverse

# Create your models here.
# each data model is a class associated with a data base table with the same data

class Article(models.Model):
    '''Data of the article'''

    # define data atributes with variable and data type
    title = models.TextField(blank=True) # can be empty
    author = models.TextField(blank=True)
    text = models.TextField(blank=True)
    published = models.DateTimeField(auto_now=True) # when it was created
    image_url = models.URLField(blank=True)

# after this, run python manage.py makemigrations to create a new file of data tables with id
# run python manage.py migrate -> features needed
# python manage.py createsuperuser

    def __str__(self):
        '''String representation of model'''
        return f'{self.title} by {self.author}'
    
# Query from terminal: python manage.py shell
# from blog.models import *
# Article.objects.all()
# similar to views.py functions

# -------------------------------------------
# to redirect where the form submission leads
    def get_absolute_url(self):
        '''Return URL to show one instance'''
        return reverse('article', kwargs={'pk':self.pk})
    
    # method to retrieve the comments
    def get_all_comments(self):
        comments = Comment.objects.filter(article=self)
        return comments


class Comment(models.Model):
    '''Comments on an article'''

    # Unique identifier for ONE instance of the article
    # if the article is deletes, ALL comments on it are deleted => cascade
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.TextField(blank=False) # already defined
    text = models.TextField(blank=False)
    published = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''Return comment string'''
        return f'{self.text}'