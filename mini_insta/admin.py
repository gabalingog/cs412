# File: mini_insta/admin.py
# Author: Gab Alingog (galingog@bu.edu), 10/01/2026
# Description: Register models

from django.contrib import admin

# Register your models here.
from .models import Profile
admin.site.register(Profile)