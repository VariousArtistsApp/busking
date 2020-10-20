import graphene

from album.mutations import CreateRelease, UpdateRelease
from album.type import AlbumType

from .models import Album


class Query(graphene.ObjectType):
    all_albums = graphene.List(AlbumType)
    album_by_name = graphene.Field(AlbumType, name=graphene.String(required=True))  # noqa E501

    def resolve_all_albums(root, info):
        return Album.objects.all()

    def resolve_album_by_name(root, info, name):
        try:
            return Album.objects.get(name=name)
        except Album.DoesNotExist:
            return None


class Mutation(graphene.ObjectType):
    create_release = CreateRelease.Field()
    update_release = UpdateRelease.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
