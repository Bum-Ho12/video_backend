"""
file: videos/models.py
location: videos/models.py
"""

from django.db import models
# pylint:disable=E0401
from cloudinary.models import CloudinaryField  # type: ignore

class Video(models.Model):
    '''
    class: Video
    description: This class is used to create a model for the video object.
    '''
    title = models.CharField(max_length=255,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    video_file = CloudinaryField('video_file', resource_type='video')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.upload_date}'
