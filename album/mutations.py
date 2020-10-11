import graphene
from album.type import AlbumType
from album.models import Album


class CreateReleaseInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    date = graphene.String(required=True)
    credits = graphene.String(required=True)
    artistName = graphene.String(required=True)
    labelName = graphene.String(required=True)
    tracks = graphene.List(graphene.String)


class InitializeRelease(graphene.Mutation):
    class Arguments:
        pass

    release = graphene.Field(AlbumType)

    def mutate(root, info, data=None):
        return InitializeRelease(release=Album.objects.create())


class CreateRelease(graphene.Mutation):
    class Arguments:
        data = CreateReleaseInput(required=True)

    album = graphene.Field(AlbumType)

    def mutate(root, info, data=None):
        Album.objects.create()
