from django.db import models

# Create your models here.
class Joke(models.Model):
    '''Stores the text of the jokes, name of contributer, and timestamp'''
    text = models.TextField()
    name = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''String representation'''
        return f'{self.text} {self.name}'

class Picture(models.Model):
    '''Stores the image's url, name of contributer, and timestamp'''
    image_url = models.URLField()
    name = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''String representation'''
        return f'{self.image_url} {self.name}'