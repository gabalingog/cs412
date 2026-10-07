# File: mini_insta/urls.py
# Author: Gab Alingog (galingog@bu.edu), 10/01/2026
# Description: Functions for each of the web pages

from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView

# Create your views here.
class ProfileListView(ListView):
    model = Profile
    template_name = 'mini_insta/show_all_profiles.html'
    context_object_name = 'profiles'

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'mini_insta/show_profile.html'
    context_object_name = 'profile'

class PostDetailView(DetailView):
    '''Single post'''
    model = Post
    template_name = 'mini_insta/show_post.html'
    context_object_name = 'post'

    # def get_context_data(self, **kwargs):
    #     '''Return context to use in templates'''
    #     context = super().get_context_data(**kwargs) # dictionary

    #     # know which post
    #     pk = self.kwargs['pk']
    #     post = Post.objects.get(pk=pk)

    #     # add profile to context
    #     context['profile'] = post.profile
    #     return context