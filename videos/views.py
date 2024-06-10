"""
file: videos/views.py
location: videos/views.py
"""
import json
from django.shortcuts import render,redirect,get_object_or_404
# from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
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

# frontend uploading scenario

def upload_video_front_view(request):
    '''
    method: upload_video_front_view
    description: This method renders the frontend video upload page.
    '''
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the video metadata to the database
            video = form.save()
            return JsonResponse({'success': True,
                'message': 'Video uploaded successfully.', 'video_id': video.id})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = VideoForm()
    return render(request, 'upload_video.html', {'form': form})

@csrf_exempt
def save_video_metadata(request):
    '''
    method: save_video_metadata
    description: This method saves video metadata after Cloudinary upload.
    '''
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title')
        description = data.get('description')
        video_file = data.get('video_file')
        # pylint:disable=E1101
        video = Video.objects.create(title=title, description=description, video_file=video_file)
        return JsonResponse({'id': video.id, 'title': video.title, 'description': video.description,
                    'video_file': video.video_file.url})
    return JsonResponse({'error': 'Invalid request'}, status=400)
