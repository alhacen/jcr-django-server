from storages.backends.s3boto3 import S3Boto3Storage
from __jcr__.secret import SECRET


class StaticStorage(S3Boto3Storage):
    location = SECRET['AWS']['S3']['STATIC_FOLDER']


class MediaStorage(S3Boto3Storage):
    location = SECRET['AWS']['S3']['MEDIA_FOLDER']
