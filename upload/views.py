from label.models import Label
from artist.models import Artist
from django.http import JsonResponse


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
