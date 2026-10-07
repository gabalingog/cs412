# File: mini_insta/urls.py
# Author: Gab Alingog (galingog@bu.edu), 10/07/2026
# Description: Functions for each of the web pages

from .models import *
from django.views.generic import ListView, DetailView, CreateView
from .forms import *

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

class CreatePostView(CreateView):
    '''Create a new post for a profile'''
    form_class = CreatePostForm
    template_name = 'mini_insta/create_post_form.html'

    def get_context_data(self):
        '''Return context to use in templates'''
        context = super().get_context_data() # dictionary
        # know which profile
        pk = self.kwargs['pk']
        profile = Profile.objects.get(pk=pk)
        # add profile to context
        context['profile'] = profile
        return context
    
    def form_valid(self, form):
        '''Handles the form submission'''
        # retrieve the identifier
        pk = self.kwargs['pk']
        profile = Profile.objects.get(pk=pk)
        # instance of whichever model
        form.instance.profile = profile
        post = form.save()

        # Old instructions ----------------------------
        # image_url = self.request.POST.get('image_url')
        # if image_url: # check if it exists
        #     Photo.objects.create(post=post, image_url=image_url)

        files = self.request.FILES.getlist('files')
        for x in files:
            Photo.objects.create(post=post, image_file=x)

        # make the superclass method return it
        return super().form_valid(form)