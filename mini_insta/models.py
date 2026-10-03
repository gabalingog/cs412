# File: mini_insta/models.py
# Author: Gab Alingog (galingog@bu.edu), 10/01/2026
# Description: Models needed

from django.db import models

# Create your models here.
class Profile(models.Model):
    username = models.TextField(blank=False)
    display_name = models.TextField(blank=False)
    profile_image_url = models.TextField(blank=False)
    bio_text = models.TextField(blank=False)
    join_date = models.TextField(blank=False)

    def __str__(self):
        return f'{self.username} ({self.display_name})'