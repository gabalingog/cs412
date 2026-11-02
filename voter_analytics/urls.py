# File: urls.py
# Author: Gab Alingog (galingog@bu.edu), 11/01/2026
# Description: URLs of the application

from django.urls import path
from . import views

urlpatterns = [
    path('', views.VotersListView.as_view(), name='voters'),
    path('graphs', views.ResultListView.as_view(), name='graphs'),
    path('voter/<int:pk>', views.VoterDetailView.as_view(), name='voter'),
]