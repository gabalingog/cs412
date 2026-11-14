from rest_framework import serializers
from .models import *

class JokeSerializer(serializers.ModelSerializer):
    '''Serializer for the joke model, specified which model/fields to send to the API'''
    class Meta:
        model = Joke
        fields = ['id', 'text', 'name', 'timestamp']

class PictureSerializer(serializers.ModelSerializer):
    '''Serializer for the picture model, specified which model/fields to send to the API'''
    class Meta:
        model = Picture
        fields = ['id', 'image_url', 'name', 'timestamp']