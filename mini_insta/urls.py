# File: mini_insta/urls.py
# Author: Gab Alingog (galingog@bu.edu), 10/01/2026
# Description: Path names and configuration of the website

from django.urls import path
from django.conf import settings
from .views import *

urlpatterns = [
    path('', ProfileListView.as_view(), name='show_all_profiles'),
    path('profile/<int:pk>', ProfileDetailView.as_view(), name='show_profile'),
    path('post/<int:pk>', PostDetailView.as_view(), name='show_post'),
    path('profile/<int:pk>/create_post', CreatePostView.as_view(), name='create_post'),
]