# File: mini_insta/models.py
# Author: Gab Alingog (galingog@bu.edu), 10/01/2026
# Description: Models needed

from django.db import models
from django.urls import reverse

# Create your models here.
class Profile(models.Model):
    '''Data for the profiles of the user'''
    username = models.TextField(blank=False)
    display_name = models.TextField(blank=False)
    profile_image_url = models.TextField(blank=False)
    bio_text = models.TextField(blank=False)
    join_date = models.TextField(blank=False)

    def __str__(self):
        '''Return the string'''
        return f'{self.username} ({self.display_name})'
    
    def get_all_posts(self):
        '''Finds all posts under a profile and returns a QuerySet'''
        return Post.objects.filter(profile=self).order_by('timestamp')

class Post(models.Model):
    '''Attributes of the users' Instagram post'''
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    caption = models.TextField(blank=True)

    def __str__(self):
        return f'{self.profile.username}{self.caption}'
    
    def get_all_photos(self):
        '''Finds all photos under a post and returns a QuerySet'''
        return Photo.objects.filter(post=self)
    
    def get_absolute_url(self):
        '''Return URL to show one instance'''
        return reverse('show_post', kwargs={'pk':self.pk})
    
class Photo(models.Model):
    '''Image with the post'''
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image_url = models.TextField(blank=False)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.post.pk} {self.image_url}'