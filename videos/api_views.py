"""
file: videos/views.py
location: videos/views.py
"""
from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Video
from .serializers import VideoSerializer


class VideoUploadView(APIView):
    '''
    class: VideoUploadView
    description: This class is used to upload a video file.
    '''
    parser_classes = (MultiPartParser, FormParser)

    # pylint:disable=unused-argument,R0201
    def post(self, request, *args, **kwargs):
        '''
        method: post
        description: This method is used to upload a video file.
        '''
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VideoListCreateAPIView(generics.ListCreateAPIView):
    '''
    class: VideoListCreateAPIView
    description: This class is used to list and create video objects.
    '''
    # pylint:disable=E1101
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class VideoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    '''
    class: VideoRetrieveUpdateDestroyAPIView
    description: This class is used to retrieve, update, and destroy video objects.
    '''
    # pylint:disable=E1101
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
