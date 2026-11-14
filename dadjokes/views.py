from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
import random
from .models import *

# Create your views here.
class RandomView(TemplateView):
    '''Show one Joke and one Picture selected at random'''
    template_name = 'dadjokes/random.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['joke'] = random.choice(Joke.objects.all())
        context['picture'] = random.choice(Picture.objects.all())
        return context
    
class JokesView(ListView):
    '''Show a page with all Jokes (no images)'''
    model = Joke
    template_name = 'dadjokes/jokes.html'
    context_object_name = 'jokes'

class JokeDetailView(DetailView):
    '''Show one Joke by its primary key'''
    model = Joke
    template_name = 'dadjokes/joke.html'
    context_object_name = 'joke'

class PicturesView(ListView):
    '''Show a page with all Pictures (no jokes)'''
    model = Picture
    template_name = 'dadjokes/pictures.html'
    context_object_name = 'pictures'

class PictureDetailView(DetailView):
    '''Show one Picture by its primary key'''
    model = Picture
    template_name = 'dadjokes/picture.html'
    context_object_name = 'picture'