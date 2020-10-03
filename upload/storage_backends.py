from storages.backends.s3boto3 import S3Boto3Storage


class PublicStorage(S3Boto3Storage):
    location = ''
    default_acl = 'public-read'