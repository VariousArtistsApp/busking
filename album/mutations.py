from datetime import datetime

import graphene

from album.models import Album
from album.type import AlbumType
from artist.models import Artist
from track.models import Track


class ReleaseTrackInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    price = graphene.Float(required=True)
    id = graphene.String(required=True)
    artists = graphene.List(graphene.String, required=True)


class CreateReleaseInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    date = graphene.String(required=True)
    description = graphene.String(required=True)


class UpdateReleaseInput(CreateReleaseInput):
    id = graphene.String(required=True)
    tracks = graphene.List(ReleaseTrackInput, required=True)


class CreateRelease(graphene.Mutation):
    class Arguments:
        data = CreateReleaseInput(required=True)

    release = graphene.Field(AlbumType)

    def mutate(root, info, data=None):
        release = Album.objects.create(name=data.name,
                                    #   date=datetime.strptime(data.date, "%d.%m.%Y"), # noqa E501
                                       description=data.description)
        return CreateRelease(release=release)


class UpdateRelease(graphene.Mutation):
    class Arguments:
        data = UpdateReleaseInput(required=True)

    release = graphene.Field(AlbumType)

    def mutate(root, info, data=None):
        try:
            release = Album.objects.get(id=data.id)
        except Album.DoesNotExist:
            raise Exception("Album??")
        release.name = data.name
        release.date = datetime.strptime(data.date, "%d.%m.%Y")
        release.description = data.description
        release_tracks = []
        for track in data.tracks:
            item = Track.objects.get(id=track.id)
            item.name = track.name
            item.price = track.price * 100  # eur to credits
            item.artists.set([Artist.objects.get(id=id) for id in track.artists])  # noqa E501
            item.save()
            release_tracks.append(item)
        release.tracks.set(release_tracks, clear=True)
        release.save()
        return UpdateRelease(release=Album.objects.first())
