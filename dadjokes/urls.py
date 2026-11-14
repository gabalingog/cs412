from django.urls import path
from .views import *

urlpatterns = [
    path('', RandomView.as_view(), name='main'),
    path('random', RandomView.as_view(), name='random'),
    path('jokes', JokesView.as_view(), name='jokes'),
    path('joke/<int:pk>', JokeDetailView.as_view(), name='joke'),
    path('pictures', PicturesView.as_view(), name='pictures'),
    path('picture/<int:pk>', PictureDetailView.as_view(), name='picture')
]