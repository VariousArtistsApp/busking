import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    label_profile = models.OneToOneField(
        'label.Label',
        on_delete=models.CASCADE,
        null=True
    )
    artist_profile = models.OneToOneField(
        'artist.Artist',
        on_delete=models.CASCADE,
        null=True
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50, unique=True)
    profile_picture = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    auto_pay = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    dob = models.DateField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
