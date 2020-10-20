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


class UpdateReleaseInput(graphene.InputObjectType):
    id = graphene.String(required=True)
    name = graphene.String(required=True)
    date = graphene.String(required=True)
    credits = graphene.String(required=True)
    artistName = graphene.String()
    labelName = graphene.String()
    tracks = graphene.List(ReleaseTrackInput, required=True)


class InitializeRelease(graphene.Mutation):
    class Arguments:
        pass

    release = graphene.Field(AlbumType)

    def mutate(root, info, data=None):
        return InitializeRelease(release=Album.objects.create())


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
        release.description = data.credits
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
        return UpdateRelease(release=release)
