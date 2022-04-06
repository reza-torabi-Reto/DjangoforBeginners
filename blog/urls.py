from pickletools import UP_TO_NEWLINE
from unicodedata import name
from django.urls import path
from django.views import *

from blog.views import BlogListView, DetailPost, CreatePost, UpdatePost, DeletePost

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>', DetailPost.as_view(), name='detail-post'),
    path('new/', CreatePost.as_view(), name='new-post'),
    path('update/<int:pk>', UpdatePost.as_view(), name='update-post'),
    path('delete/<int:pk>', DeletePost.as_view(), name='delete-post'),
    
]