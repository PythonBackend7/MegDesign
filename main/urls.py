from django.urls import path
from .views import *

urlpatterns = [
    path('author/', AuthorListview.as_view(), name='author'),
    path('authordetail/', AuthorDetailView.as_view(), name='authordetail'),
    path('catigory/', CategoryListview.as_view(), name='category'),
    path('post/', PostListview.as_view(), name='post'),
    path('postdetail/', PostDetailView.as_view(), name='postdetail'),
    path('postimages/', PostImageListview.as_view(), name='postimages'),
    path('sicialmedia/', SocialMediaListview.as_view(), name='socialmedia'),
    path('subscribe/', SubscriberListview.as_view(), name='subscribe'),
]


