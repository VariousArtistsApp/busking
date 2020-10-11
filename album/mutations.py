import graphene
from .schema import AlbumType
from .models import Album


class CreateReleaseInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    date = graphene.String(required=True)
    credits = graphene.String(required=True)
    artistName = graphene.String(required=True)
    labelName = graphene.String(required=True)
    tracks = graphene.List(graphene.String)


class CreateAlbum(graphene.ObjectType):
    class Arguments:
        data = CreateReleaseInput(required=True)

    album = graphene.Field(AlbumType)

    def mutate(root, info, data=None):
        Album.objects.create()
