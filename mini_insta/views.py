# File: mini_insta/urls.py
# Author: Gab Alingog (galingog@bu.edu), 10/22/2026
# Description: Functions for each of the web pages

from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .forms import *
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin # authentication
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

# Create your views here.

class LoginRequired(LoginRequiredMixin):
    '''Subclass of LoginRequiredMixin with additional features'''
    
    def get_login_url(self):
        '''Return URL of the login page'''
        return reverse('login')
    
    def get_profile(self):
        return Profile.objects.filter(user=self.request.user).first()
    
class ProfileListView(ListView):
    model = Profile
    template_name = 'mini_insta/show_all_profiles.html'
    context_object_name = 'profiles'

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'mini_insta/show_profile.html'
    context_object_name = 'profile'

    def get_object(self):
        '''Depends on logged in user'''

        if 'pk' in self.kwargs:
            return super().get_object()
        return Profile.objects.filter(user=self.request.user).first()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = None
        if self.request.user.is_authenticated:
            user = Profile.objects.filter(user=self.request.user).first()
        context['my_profile'] = user
        context['is_following'] = bool(user) and Follow.objects.filter(profile=self.object, follower_profile=user).exists()
        return context

class PostDetailView(DetailView):
    '''Single post'''
    model = Post
    template_name = 'mini_insta/show_post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = None
        if self.request.user.is_authenticated:
            user = Profile.objects.filter(user=self.request.user).first()
        context['my_profile'] = user
        context['liked'] = bool(user) and Like.objects.filter(post=self.object, profile=user).exists()
        return context

class CreatePostView(LoginRequired, CreateView):
    '''Create a new post for a profile'''
    form_class = CreatePostForm
    template_name = 'mini_insta/create_post_form.html'

    def get_context_data(self, **kwargs):
        '''Return context to use in templates'''
        context = super().get_context_data(**kwargs) # dictionary
        # know which profile
        # pk = self.kwargs['pk']
        # profile = Profile.objects.get(pk=pk)
        # add profile to context
        # context['profile'] = profile
        context = super().get_context_data(**kwargs)
        context['profile'] = self.get_profile()
        return context
    
    def form_valid(self, form):
        '''Handles the form submission'''
        # retrieve the identifier
        # pk = self.kwargs['pk']
        # profile = Profile.objects.get(pk=pk)
        # instance of whichever model
        # form.instance.profile = profile
        form.instance.profile = self.get_profile()
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

    def get_object(self):
        return self.get_profile()

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

    def get_object(self):
        return self.get_profile()

class SearchView(LoginRequired, ListView):
    '''Search feature based on text for the user'''
    template_name = 'mini_insta/search_results.html'
    context_object_name = 'posts'

    def dispatch(self, request, *args, **kwargs):
        '''Handles any request from user'''

        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if 'query' not in self.request.GET:
            # pk = self.kwargs['pk']
            # profile = Profile.objects.get(pk=pk)
            return render(request, 'mini_insta/search.html', {'profile': self.get_profile()})
        
        return super().dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        '''Get the QuerySet of the instance data'''
        query = self.request.GET.get('query', '')
        return Post.objects.filter(caption__icontains=query).order_by('-timestamp')
    
    def get_context_data(self, **kwargs):
        '''Returns the context data for templates'''
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('query', '')

        # pk = self.kwargs['pk']
        # context['profile'] = Profile.objects.get(pk=pk)
        context['profile'] = self.get_profile()
        context['query'] = query
        context['posts'] = self.get_queryset()

        find_username = Profile.objects.filter(username__icontains=query)
        find_display = Profile.objects.filter(display_name__icontains=query)
        find_bio = Profile.objects.filter(bio_text__icontains=query)
        profiles = set(find_username) | set(find_display) | set(find_bio)
        context['profiles'] = list(profiles)
        return context
    
class LoggedOutView(TemplateView):
    '''Confirmation from logging out'''
    template_name = 'mini_insta/logged_out.html'

class CreateProfileView(CreateView):
    '''Create new profile user'''
    template_name = 'mini_insta/create_profile_form.html'
    form_class = CreateProfileForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_create_form'] = UserCreationForm()
        return context
    
    def form_valid(self, form):
        user_create = UserCreationForm(self.request.POST)
        user = user_create.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        form.instance.user = user
        return super().form_valid(form)

class ProfileFollowView(LoginRequired, TemplateView):
    '''Check profile followings'''
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        user = self.get_profile()
        other = Profile.objects.get(pk=self.kwargs['pk'])
        if user != other and not Follow.objects.filter(profile=other, follower_profile=user).exists():
            Follow.objects.create(profile=other, follower_profile=user)
        return redirect('show_profile', pk=other.pk)
    
class DeleteFollowView(LoginRequired, TemplateView):
    '''Unfollowing profiles'''
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        user = self.get_profile()
        other = Profile.objects.get(pk=self.kwargs['pk'])
        Follow.objects.filter(profile=other, follower_profile=user).delete()
        return redirect('show_profile', pk=other.pk)

class PostLikesView(LoginRequired, TemplateView):
    '''Profile likes a post'''
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        user = self.get_profile()
        post = Post.objects.get(pk=self.kwargs['pk'])
        if post.profile != user and not Like.objects.filter(post=post, profile=user).exists():
            Like.objects.create(post=post, profile=user)
        return redirect('show_post', pk=post.pk)

class DeleteLikePostView(LoginRequired, TemplateView):
    '''Profile removes a like from a post'''
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        user = self.get_profile()
        post = Post.objects.get(pk=self.kwargs['pk'])
        Like.objects.filter(post=post, profile=user).delete()
        return redirect('show_post', pk=post.pk)