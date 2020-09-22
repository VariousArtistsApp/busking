from django.db import models
from django.contrib.postgres.fields import ArrayField
import uuid

class Album(models.Model):

  #suggested_albums
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=150, null=True, blank=True)
  release_date = models.DateTimeField()
  cost = models.IntegerField(default=0)
  total_listens = models.IntegerField(default=0)
  artwork = ArrayField(models.CharField(max_length=150))
  tracks = models.ManyToManyField('track.Track', blank=True)
  label =  models.ForeignKey('label.Label', on_delete=models.SET_NULL, null=True, blank=True)
  tags =  models.ManyToManyField('tag.Tag', blank=True)
  bandcamp_link = models.CharField(max_length=150,null=True, blank=True)
  beatport_link = models.CharField(max_length=150,null=True, blank=True)
  
  def get_artists(self):
      return ''
    
  def __str__(self):
      return self.name
