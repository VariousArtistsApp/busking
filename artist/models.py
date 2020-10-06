from django.db import models
from busking import settings
import uuid
from upload.storage_backends import PublicStorage


def get_profile_picture_path(instance, filename):
    if settings.DEBUG:
        return "test/profiles/artist_{0}/{1}".format(instance.id, filename)
    else:
        return "profiles/artist_{0}/{1}".format(instance.id, filename)


class Artist(models.Model):
    # admin
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tags = models.ManyToManyField('tag.Tag', blank=True) 
    followers = models.ManyToManyField('user.CustomUser', blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile_picture = models.FileField(upload_to=get_profile_picture_path,
                                       storage=PublicStorage())
    location = models.CharField(max_length=150)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150, null=True, blank=True)
    albums = models.ManyToManyField('album.Album', blank=True)
    facebook_link = models.CharField(max_length=150,null=True, blank=True)
    twitter_link = models.CharField(max_length=150,null=True, blank=True)
    bandcamp_link = models.CharField(max_length=150,null=True, blank=True)
    soundcloud_link = models.CharField(max_length=150,null=True, blank=True)
    beatport_link = models.CharField(max_length=150,null=True, blank=True)
    
    def __str__(self):
        return self.name