from rest_framework import viewsets

from .serializers import *
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .models import *


# Create your views here.

class HomeView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostViewSet(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class AuthorView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class Social_MediaView(ListAPIView):
    queryset = Social_Media.objects.all()
    serializer_class = Social_MediaSerializer


class CategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TrendingView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class MostPopularView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
