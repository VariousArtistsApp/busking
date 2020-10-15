import uuid

from django.contrib.postgres.fields import ArrayField
from django.db import models


class Album(models.Model):

    # suggested_albums
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=150, null=True, blank=True)
    release_date = models.DateTimeField(auto_now_add=True)
    cost = models.IntegerField(default=0)
    total_listens = models.IntegerField(default=0)
    artwork = ArrayField(models.CharField(max_length=150), blank=True, null=True)  # noqa E501
    tracks = models.ManyToManyField('track.Track', blank=True)
    label = models.ForeignKey('label.Label', on_delete=models.SET_NULL, null=True, blank=True)  # noqa E501
    tags = models.ManyToManyField('tag.Tag', blank=True)
    bandcamp_link = models.CharField(max_length=150, null=True, blank=True)
    beatport_link = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        if self.name:
            return self.name
        return str(self.id)
