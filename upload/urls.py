from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import upload_profile_picture, upload_tracks

app_name = "upload"

urlpatterns = [
    path('profilePicture', csrf_exempt(upload_profile_picture)),
    path('tracks', csrf_exempt(upload_tracks))
]
