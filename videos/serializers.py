"""
file: serializers.py
location: videos/serializers.py
"""

from rest_framework import serializers
from .models import Video

class VideoSerializer(serializers.ModelSerializer):
    '''
    class: VideoSerializer
    description: This class is used to serialize the video object.
    '''
    class Meta:
        '''
        class: Meta
        description: This class is used to define the fields for the serializer.
        '''
        model = Video
        fields = '__all__'
