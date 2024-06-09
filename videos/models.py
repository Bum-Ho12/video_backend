"""
file: videos/models.py
location: videos/models.py
"""

from django.db import models

class Video(models.Model):
    '''
    class: Video
    description: This class is used to create a model for the video object.
    '''
    title = models.CharField(max_length=255,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    video_file = models.FileField(upload_to='videos')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.upload_date}'
