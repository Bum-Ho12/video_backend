"""
file:urls.py
location:videos/urls.py
"""
from django.urls import path
from . import views
from .api_views import (VideoListCreateAPIView,VideoUploadView,
VideoRetrieveUpdateDestroyAPIView)

urlpatterns = [
    path('', views.video_list, name='video_list'),
    path('upload/', views.upload_video, name='upload_video'),
    path('<int:pk>/', views.video_detail, name='video_detail'),
    path('api/videos/', VideoListCreateAPIView.as_view(), name='api_video_list_create'),
    path('api/videos/<int:pk>/',
        VideoRetrieveUpdateDestroyAPIView.as_view(), name='api_video_detail'
    ),
    path('api/videos/upload/', VideoUploadView.as_view(), name='api_video_upload'),
]
