import uuid

from django.db import models

from busking import settings


def get_track_path(instance, filename):
    if settings.DEBUG:
        return "test/releases/{0}/{1}".format(instance.location, filename)
    else:
        return "profiles/{0}/{1}".format(instance.location, filename)


class Track(models.Model):
    # playList
    # likes
    # tags
    artists = models.ManyToManyField('artist.Artist', blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # TODO max_length here isn't working!! bug!
    file = models.FileField(max_length=255, upload_to=get_track_path)
    picture = models.CharField(max_length=150, blank=True, null=True)
    location = models.CharField(max_length=150, blank=True, null=True)
    total_listens = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150, null=True, blank=True)
