# from django.shortcuts import render
from .models import Article
from django.views.generic import ListView, DetailView, CreateView # -> single instance of one model
import random
from .forms import *

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