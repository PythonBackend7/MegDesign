from rest_framework import serializers
from .models import *


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class Social_MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social_Media
        fields = ['title']


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'


class Extra_ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extra_Images
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    social_media = Social_MediaSerializer(read_only=True, many=True)
    subscriber = SubscriberSerializer(read_only=True, many=True)
    extra_images = Extra_ImagesSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = '__all__'
