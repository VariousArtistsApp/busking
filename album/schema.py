import graphene
from graphene_django import DjangoObjectType

from .models import Album

class AlbumType(DjangoObjectType):
    class Meta:
        model = Album


class Query(graphene.ObjectType):
    all_albums = graphene.List(AlbumType)
    album_by_name = graphene.Field(AlbumType, name=graphene.String(required=True))

    def resolve_all_albums(root, info):
        return Album.objects.all()

    def resolve_album_by_name(root, info, name):
        try:
            return Album.objects.get(name=name)
        except Category.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)