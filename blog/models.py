from django.db import models

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