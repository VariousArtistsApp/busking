import uuid

from django.db import models


class Tag(models.Model):
    # albums
    # tracks
    # artists
    # labels
    # followers
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150, null=True, blank=True)
