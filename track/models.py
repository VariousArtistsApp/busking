from django.db import models
import uuid
class Track(models.Model):
  #albums
  #artists
  #playList
  #likes 
  #tags
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  file = models.FileField()
  picture = models.CharField(max_length=150)
  location = models.CharField(max_length=150)
  total_listens = models.IntegerField(default=0)
  cost = models.IntegerField()
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=150, null=True, blank=True)
