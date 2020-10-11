from graphene_django import DjangoObjectType
from album.models import Album


class AlbumType(DjangoObjectType):
    class Meta:
        model = Album
