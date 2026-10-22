# File: mini_insta/urls.py
# Author: Gab Alingog (galingog@bu.edu), 10/22/2026
# Description: Functions for each of the web pages

from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import *
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin # authentication

# Create your views here.

class LoginRequired(LoginRequiredMixin):
    '''Subclass of LoginRequiredMixin with additional features'''

    def get_profile(self):
        return Profile.objects.get(user=self.request.user)
    
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

class CreatePostView(LoginRequired, CreateView):
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
    
class UpdateProfileView(LoginRequired, UpdateView):
    '''Updates the profile of user'''
    model = Profile
    form_class = UpdateProfileForm
    template_name = 'mini_insta/update_profile_form.html'

class DeletePostView(LoginRequired, DeleteView):
    '''Deletes a post from the user'''
    model = Post
    template_name = 'mini_insta/delete_post_form.html'

    def get_context_data(self, **kwagrs):
        '''Return context to use in templates'''
        context = super().get_context_data(**kwagrs) # dictionary
        # know which post and profile
        pk = self.kwargs['pk']
        post = Post.objects.get(pk=pk)
        # add profile to context
        context['post'] = post
        context['profile'] = post.profile
        return context
    
    def get_success_url(self):
        '''Redirects to the correct url'''
        pk = self.kwargs['pk']
        post = Post.objects.get(pk=pk)
        return reverse('show_profile', kwargs={'pk':post.profile.pk})
    
class UpdatePostView(LoginRequired, UpdateView):
    '''Updates a post of a user'''
    model = Post
    form_class = UpdatePostForm
    template_name = 'mini_insta/update_post_form.html'

class ShowFollowersDetailView(DetailView):
    '''Shows followers of a profile'''
    model = Profile
    template_name = 'mini_insta/show_followers.html'
    context_object_name = 'profile'

class ShowFollowingDetailView(DetailView):
    '''Shows following of a profile'''
    model = Profile
    template_name = 'mini_insta/show_following.html'
    context_object_name = 'profile'

class ShowFeedView(LoginRequired, DetailView):
    '''Show feed for a profile'''
    model = Profile
    template_name = 'mini_insta/show_feed.html'
    context_object_name = 'profile'

class SearchView(LoginRequired, ListView):
    '''Search feature based on text for the user'''
    template_name = 'mini_insta/search_results.html'
    context_object_name = 'posts'

    def dispatch(self, request, *args, **kwargs):
        '''Handles any request from user'''
        if 'query' not in self.request.GET:
            pk = self.kwargs['pk']
            profile = Profile.objects.get(pk=pk)
            return render(request, 'mini_insta/search.html', {'profile': profile})
        
        return super().dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        '''Get the QuerySet of the instance data'''
        query = self.request.GET.get('query', '')
        return Post.objects.filter(caption__icontains=query).order_by('-timestamp')
    
    def get_context_data(self, **kwargs):
        '''Returns the context data for templates'''
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('query', '')

        pk = self.kwargs['pk']
        context['profile'] = Profile.objects.get(pk=pk)
        context['query'] = query
        context['posts'] = self.get_queryset()

        find_username = Profile.objects.filter(username__icontains=query)
        find_display = Profile.objects.filter(display_name__icontains=query)
        find_bio = Profile.objects.filter(bio_text__icontains=query)
        profiles = set(find_username) | set(find_display) | set(find_bio)
        context['profiles'] = list(profiles)
        return context