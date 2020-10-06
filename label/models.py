from django.contrib.postgres.fields import ArrayField
from django.db import models
import uuid
from busking import settings
from upload.storage_backends import PublicStorage


def get_profile_picture_path(instance, filename):
    if settings.DEBUG:
        return "test/profiles/label_{0}/{1}".format(instance.id, filename)
    else:
        return "profiles/label_{0}/{1}".format(instance.id, filename)


class Label(models.Model):
    # admins
    tags = models.ManyToManyField('tag.Tag', blank=True)
    artists = models.ManyToManyField('artist.Artist', blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    discount_codes = ArrayField(models.CharField(max_length=150), null=True,
                                blank=True)
    subscription_cost = models.IntegerField(null=True)
    profile_picture = models.FileField(upload_to=get_profile_picture_path,
                                       storage=PublicStorage())
    location = models.CharField(max_length=150)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    description = models.CharField(max_length=150, null=True, blank=True)
    facebook_link = models.CharField(max_length=150, null=True, blank=True)
    twitter_link = models.CharField(max_length=150, null=True, blank=True)
    bandcamp_link = models.CharField(max_length=150, null=True, blank=True)
    soundcloud_link = models.CharField(max_length=150, null=True, blank=True)
    beatport_link = models.CharField(max_length=150, null=True, blank=True)
    