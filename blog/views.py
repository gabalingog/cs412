# from django.shortcuts import render
from .models import Article
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView # -> single instance of one model
import random
from .forms import *
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin # authentication
from django.contrib.auth.forms import UserCreationForm # new user
from django.contrib.auth.models import User # user model from django

# Create your views here.

# views for the app
class ShowAllView(ListView):
    '''Create a subclass of ListView to display articles'''

    model = Article # retrieve objects from the database
    template_name = 'blog/show_all.html'
    context_object_name = 'articles'

    def dispatch(self, request, *args, **kwargs):
        '''Override the dispatch method to add debugging information'''

        if request.user.is_authenticated:
            print(f'ShowAllView.dispatch(): request.user={request.user}')
        else:
            print(f'ShowAllView.dispatch(): not logged in')
        return super().dispatch(request, *args, **kwargs)

class ArticleView(DetailView):
    '''One model'''

    model = Article
    template_name = "blog/article.html"
    context_object_name = 'article' # different

class RandomArticleView(DetailView):
    '''Random single article'''

    model = Article
    template_name = "blog/article.html"
    context_object_name = 'article'

    # method under detail view
    def get_object(self):
        all_articles = Article.objects.all()
        article = random.choice(all_articles)
        return article
    
class CreateArticleView(LoginRequiredMixin, CreateView):
    # cant create if not logged in
    '''handle new article
    1. display HTML form to user (GET)
    2. process the form submission and store the new article (POST)
    '''
    form_class = CreateArticleForm
    template_name = 'blog/create_article_form.html'

    def form_valid(self, form):
        print(f'CreateArticleView.form_valid(): {form.cleaned_data}')

        # find logged in user and attach to form instance (Article object)
        user = self.request.user
        print(f'CreateArticleView.form_valid(): {user}')

        form.instance.user = user

        return super().form_valid(form)
    
    def get_login_url(self):
        '''Return url for login page'''
        return reverse('login')

# method to display create comment form
class CreateCommentView(CreateView):
    form_class = CreateCommentForm
    template_name = 'blog/create_comment_form.html'

    def get_success_url(self):
        '''Redict after a new comment submitted'''
        pk = self.kwargs['pk']
        # find url needed with reverse
        return reverse('article', kwargs={'pk':pk})
    
    def form_valid(self, form):
        '''Handles form submission and saves the new object
        Needs foreign key of the article to know where the comment is placed'''

        # retrieve the identifier
        pk = self.kwargs['pk']
        article = Article.objects.get(pk=pk)
        # instance of whichever model
        form.instance.article = article

        # make the superclass method return it
        return super().form_valid(form)


    def get_context_data(self):
        '''Return context to use in templates'''
        context = super().get_context_data() # dictionary

        # know which article
        pk = self.kwargs['pk']
        article = Article.objects.get(pk=pk)

        # add article to context
        context['article'] = article
        return context
    
class UpdateArticleView(UpdateView):
    model = Article
    form_class = UpdateArticleForm
    template_name = 'blog/update_article_form.html'

class DeleteCommentView(DeleteView):
    model = Comment
    template_name = 'blog/delete_comment_form.html'

    def get_success_url(self):
        # find the pk for the comment
        pk = self.kwargs['pk']

        # find the comment object
        comment = Comment.objects.get(pk=pk)

        # find the pk of the article
        article = comment.article
        return reverse('article', kwargs={'pk':article.pk})

class UserRegistrationView(CreateView):
    '''Show/process the registration form to create a new user'''

    template_name = 'blog/register.html'
    form_class = UserCreationForm
    model = User

    def get_success_url(self):
        '''URL Redirection after creation'''
        return reverse('login')