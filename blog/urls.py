from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/', CategoryView.as_view(), name='category'),
    path('author/', AuthorView.as_view(), name='author'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post'),
    path('post/', PostViewSet.as_view(), name='post1')
]
