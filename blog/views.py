# from django.shortcuts import render
from .models import Article
from django.views.generic import ListView, DetailView, CreateView # -> single instance of one model
import random
from .forms import *
from django.urls import reverse

# Create your views here.

# views for the app
class ShowAllView(ListView):
    '''Create a subclass of ListView to display articles'''

    model = Article # retrieve objects from the database
    template_name = 'blog/show_all.html'
    context_object_name = 'articles'

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
    
class CreateArticleView(CreateView):
    '''handle new article
    1. display HTML form to user (GET)
    2. process the form submission and store the new article (POST)
    '''
    form_class = CreateArticleForm
    template_name = 'blog/create_article_form.html'

    def form_valid(self, form):
        return super().form_valid(form)

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