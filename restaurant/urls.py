# File: urls.py
# Author: Gab Alingog (galingog@bu.edu), 09/12/2026
# Description: Path names and configuration of the website

from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path(r'main', views.main, name='main'),
    path(r'order', views.order, name='order'),
    path(r'confirmation', views.confirmation, name='confirmation'),
]