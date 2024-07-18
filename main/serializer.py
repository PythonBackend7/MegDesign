from rest_framework import serializers
from  .models import Author, Post, PostImage, Subscribe, SocialMedia, Category


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class PostImagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PostImage
        fields = '__all__'


class SubsciribeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subscribe
        fields = '__all__'

class SocialMediaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

