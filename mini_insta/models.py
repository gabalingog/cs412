# File: mini_insta/models.py
# Author: Gab Alingog (galingog@bu.edu), 10/07/2026
# Description: Models needed for the application

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
    
    def get_absolute_url(self):
        '''Redirects to the correct url'''
        return reverse('show_profile', kwargs={'pk':self.pk})
    
    def get_followers(self):
        '''Returns list of users who follow a profile'''
        followers = Follow.objects.filter(profile=self)
        followers_list = [user.follower_profile for user in followers]
        return followers_list
    
    def get_num_followers(self):
        '''Return number of followers for a profile'''
        return Follow.objects.filter(profile=self).count()
    
    def get_following(self):
        '''Returns list of users that a profile follows'''
        follows = Follow.objects.filter(follower_profile=self)
        follows_list = [user.profile for user in follows]
        return follows_list
    
    def get_num_following(self):
        '''Return number of user a profile follows'''
        return Follow.objects.filter(follower_profile=self).count()

class Post(models.Model):
    '''Attributes of the users' Instagram post'''
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    caption = models.TextField(blank=True)

    def __str__(self):
        '''Return string'''
        return f'{self.profile.username}{self.caption}'
    
    def get_all_photos(self):
        '''Finds all photos under a post and returns a QuerySet'''
        return Photo.objects.filter(post=self)
    
    def get_absolute_url(self):
        '''Return URL to show one instance'''
        return reverse('show_post', kwargs={'pk':self.pk})
    
    def get_all_comments(self):
        '''Return all comments on a post'''
        return Comment.objects.filter(post=self).order_by('timestamp')
    
    def get_likes(self):
        '''All likes on a post'''
        return Like.objects.filter(post=self)
    
class Photo(models.Model):
    '''Image with the post'''
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image_url = models.TextField(blank=False)
    timestamp = models.DateTimeField(auto_now=True)
    image_file = models.ImageField(blank=True)

    def __str__(self):
        '''Return string depending on the image variable'''
        if self.image_url:
            return f'{self.post.pk} {self.image_url}'
        elif self.image_file:
            return f'{self.post.pk} {self.image_file.name}'
        else:
            return {self.post.pk}
    
    def get_image_url(self):
        '''Return the URL itself or the URL of the image file'''
        if self.image_url:
            return self.image_url
        elif self.image_file:
            return self.image_file.url
        else:
            return ''
        
class Follow(models.Model):
    '''Connects two profiles within the social network'''
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile')
    follower_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='follower_profile')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''Return string'''
        return f'{self.follower_profile.username} following {self.profile.username}'

class Comment(models.Model):
    '''Comment on a user's post'''
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=False)

    def __str__(self):
        '''Return string'''
        return f'{self.profile.username} commented {self.text} on {self.post.pk}'
    
class Like(models.Model):
    '''Like from a user on a post'''
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''Return string'''
        return f'{self.profile.username} likes {self.post.pk}'