from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
import random
from .models import *
from rest_framework import generics
from .serializer import *

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

class JokeListAPIView(generics.ListCreateAPIView):
    '''API view to return a listing of Jokes'''
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer

class JokeDetailAPIView(generics.RetrieveAPIView):
    '''One joke by its primary key'''
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer

class RandomJokeAPIView(generics.RetrieveAPIView):
    '''One random joke'''
    serializer_class = JokeSerializer

    def get_object(self):
        '''Random choice'''
        return random.choice(Joke.objects.all())

class PictureListAPIView(generics.ListAPIView):
    '''API view to return a listing of Jokes'''
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

class PictureDetailAPIView(generics.RetrieveAPIView):
    '''One picture by primary key'''
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

class RandomPictureAPIView(generics.RetrieveAPIView):
    '''One random picture'''
    serializer_class = PictureSerializer

    def get_object(self):
        '''Random choice'''
        return random.choice(Picture.objects.all())