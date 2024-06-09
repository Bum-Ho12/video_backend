"""
file: videos/views.py
location: videos/views.py
"""
from django.shortcuts import render,redirect,get_object_or_404
from .models import Video
# pylint:disable=E0401
from .forms import VideoForm


def documentation(request):
    '''
    method: documentation
    description: This method is used to render the documentation page.
    '''
    return render(request, 'documentation.html')

def upload_video(request):
    '''
    method: upload_video
    description: This class is used to upload a video file.
    '''
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = VideoForm()
    return render(request, 'upload_video.html', {'form': form})


def video_list(request):
    '''
    method: video_list
    description: This method is used to list all the video files.
    '''
    # pylint:disable=E1101
    videos = Video.objects.all()
    return render(request, 'video_list.html', {'videos': videos})

def video_detail(request, pk):
    '''
    method: video_detail
    description: This method is used to display the details of a video file.
    '''
    video = get_object_or_404(Video, pk=pk)
    return render(request, 'video_detail.html', {'video': video})
