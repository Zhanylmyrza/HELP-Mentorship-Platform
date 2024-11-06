# from storages.backends.s3boto3 import S3Boto3Storage


# class MediaStorage(S3Boto3Storage):
#     location = "media"
#     file_overwrite = False
from storages.backends.s3boto3 import S3Boto3Storage


class MediaStorage(S3Boto3Storage):
    default_acl = "public-read"
    bucket_name = "zhzh"
    location = "media/"
    region_name = "eu-north-1"
    file_overwrite = False
