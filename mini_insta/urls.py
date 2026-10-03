# File: mini_insta/urls.py
# Author: Gab Alingog (galingog@bu.edu), 10/01/2026
# Description: Path names and configuration of the website

from django.urls import path
from django.conf import settings
from .views import ProfileListView, ProfileDetailView

urlpatterns = [
    path('', ProfileListView.as_view(), name='show_all_profiles'),
    path('profile/<int:pk>', ProfileDetailView.as_view(), name='show_profile'),
]