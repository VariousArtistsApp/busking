import uuid

from django.db import models

from busking import settings


def get_cover_path(instance, filename):
    if settings.DEBUG:
        return "test/releases/{0}/{1}".format(instance._file_path, filename)
    else:
        return "releases/{0}/{1}".format(instance._file_path, filename)


class Album(models.Model):

    # suggested_albums
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=150, null=True, blank=True)
    release_date = models.DateTimeField(auto_now_add=True)
    cost = models.IntegerField(default=0)
    total_listens = models.IntegerField(default=0)
    cover = models.FileField(max_length=255, upload_to=get_cover_path, null=True, blank=True)  # noqa E501
    tracks = models.ManyToManyField('track.Track', blank=True)
    label = models.ForeignKey('label.Label', on_delete=models.SET_NULL, null=True, blank=True)  # noqa E501
    tags = models.ManyToManyField('tag.Tag', blank=True)
    bandcamp_link = models.CharField(max_length=150, null=True, blank=True)
    beatport_link = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        if self.name:
            return self.name
        return str(self.id)
