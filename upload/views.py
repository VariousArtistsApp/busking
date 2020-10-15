from django.http import JsonResponse

from artist.models import Artist
from label.models import Label
from track.models import Track


def upload_profile_picture(request):
    if request.method == "POST":
        id = request.POST["id"]
        type = request.POST["type"]
        if type == "artist":
            try:
                profile = Artist.objects.get(id=id)
            except Artist.DoesNotExist:
                raise ""
        if type == "label":
            try:
                profile = Label.objects.get(id=id)
            except Label.DoesNotExist:
                raise ""
        profile.profile_picture = request.FILES.get('profile_picture')
        profile.save()
        return JsonResponse({'response': 'success',
                             'picture_url': profile.profile_picture.url})


def upload_tracks(request):
    if request.method == "POST":
        type = "artist"
        if request.POST['type'] == "Label":
            type = "label"
        for key in request.FILES:
            track = Track.objects.create(name=key,
                                         location="{0}_{1}/{2}".format(type,
                                                                       request.POST['profile_id'],  # noqa E501
                                                                       request.POST['album_id']),   # noqa E501
                                         file=request.FILES.get(key))
        return JsonResponse({"response": "success",
                             "track": {"name": key, "id": str(track.id)}})
