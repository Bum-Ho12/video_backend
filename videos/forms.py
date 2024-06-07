"""
file: videos/forms.py
location: videos/forms.py
"""

from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    '''
    class: VideoForm
    description: This class is used to create a form for the video object.
    '''
    class Meta:
        '''
        class: Meta
        description: This class is used to define the fields for the form.
        '''
        model = Video
        fields = ['title', 'description', 'video_file']
