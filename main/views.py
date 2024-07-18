from django.shortcuts import render
from .models import *
from .serializer import *
# Create your views here.
from rest_framework import  generics


class AuthorListview(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailView(generics.RetrieveUpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class CategoryListview(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostListview(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostImageListview(generics.ListCreateAPIView):
    queryset = PostImage.objects.all()
    serializer_class = PostImagesSerializer

class SocialMediaListview(generics.ListCreateAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer

class SubscriberListview(generics.ListCreateAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubsciribeSerializer



