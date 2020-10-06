from django.urls import path
from .views import upload_profile_picture
from django.views.decorators.csrf import csrf_exempt

app_name = "upload"

urlpatterns = [
    path('profilePicture', csrf_exempt(upload_profile_picture)),
]
