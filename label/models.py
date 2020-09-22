from django.db import models
from django.contrib.postgres.fields import ArrayField
from artist.models import Artist
import uuid


class Label(models.Model):
  #admins
  tags =  models.ManyToManyField('tag.Tag', blank=True)
  artists = models.ManyToManyField('artist.Artist', blank=True)
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  discount_codes = ArrayField(models.CharField(max_length=150))
  subscription_cost = models.IntegerField()
  profile_picture = models.CharField(max_length=150)
  location = models.CharField(max_length=150)
  name = models.CharField(max_length=50)
  email = models.EmailField()
  description = models.CharField(max_length=150, null=True, blank=True)
  facebook_link = models.CharField(max_length=150,null=True, blank=True)
  twitter_link = models.CharField(max_length=150,null=True, blank=True)
  bandcamp_link = models.CharField(max_length=150,null=True, blank=True)
  soundcloud_link = models.CharField(max_length=150,null=True, blank=True)
  beatport_link = models.CharField(max_length=150,null=True, blank=True)
  