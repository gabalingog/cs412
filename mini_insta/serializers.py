from rest_framework import serializers
from .models import *

class PhotoSerializer(serializers.ModelSerializer):
    '''Serializer for the photo model, specified which model/fields to send to the API'''
    class Meta:
        model = Photo
        fields = ['id', 'image_url', 'image_file', 'timestamp']
    
class PostSerializer(serializers.ModelSerializer):
    '''Serializer for the photo model, specified which model/fields to send to the API'''
    set = PhotoSerializer(many=True, required=False)

    class Meta:
        model = Post
        exclude = ['profile']

class ProfileSerializer(serializers.ModelSerializer):
    '''Serializer for the profile model, specified which model/fields to send to the API'''
    class Meta:
        model = Profile
        fields = ['id', 'username', 'display_name', 'bio_text', 'profile_image_url', 'join_date']
