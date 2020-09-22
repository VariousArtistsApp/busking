import graphene
from graphene_django import DjangoObjectType

from .models import Artist
from album.models import Album
from album.schema import AlbumType

class ArtistType(DjangoObjectType):
    albums = graphene.List(AlbumType)
    
    @graphene.resolve_only_args
    def resolve_albums(self):
        return self.albums.all()
        
    class Meta:
        model = Artist


class Query(graphene.ObjectType):
    all_artists = graphene.List(ArtistType)
    artist_by_name = graphene.Field(ArtistType, name=graphene.String(required=True))

    def resolve_all_artists(root, info):
        return Artist.objects.all()

    def resolve_artist_by_name(root, info, name):
        try:
            return Artist.objects.get(name=name)
        except Category.DoesNotExist:
            return None
                
schema = graphene.Schema(query=Query)