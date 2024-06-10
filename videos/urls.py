"""
file:urls.py
location:videos/urls.py
"""
from django.urls import path
from . import views
from .api_views import (VideoListCreateAPIView,VideoUploadView,
VideoRetrieveUpdateDestroyAPIView)

urlpatterns = [
    path('', views.documentation, name='documentation'),  # Set documentation as the root URL
    path('videos/', views.video_list, name='video_list'),
    path('videos/upload/', views.upload_video, name='upload_video'),
    path('videos/<int:pk>/', views.video_detail, name='video_detail'),
    path('videos/front/', views.upload_video_front_view, name='upload_video_front'),
    path('save-video-metadata/', views.save_video_metadata, name='save_video_metadata'),
    path('api/videos/', VideoListCreateAPIView.as_view(), name='api_video_list_create'),
    path('api/videos/<int:pk>/',
        VideoRetrieveUpdateDestroyAPIView.as_view(), name='api_video_detail'),
    path('api/videos/upload/', VideoUploadView.as_view(), name='api_video_upload'),
]
