"""
file: standard.py
location: videos/standard.py
"""
from cloudinary_storage.storage import MediaCloudinaryStorage
import cloudinary.uploader

class VideoMediaCloudinaryStorage(MediaCloudinaryStorage):
    '''
    class: VideoMediaCloudinaryStorage
    description: This class is used to upload videos to Cloudinary.
    '''
    def _save(self, name, content):
        # Upload to Cloudinary with resource type video
        response = cloudinary.uploader.upload(content, resource_type="video")
        return response['secure_url']