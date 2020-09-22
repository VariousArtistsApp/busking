import graphene
from graphene_django import DjangoObjectType

from .models import Track

class TrackType(DjangoObjectType):
    class Meta:
        model = Track


class Query(graphene.ObjectType):
    all_tracks = graphene.List(TrackType)
    track_by_name = graphene.Field(TrackType, name=graphene.String(required=True))

    def resolve_all_tracks(root, info):
        return Track.objects.all()

    def resolve_track_by_name(root, info, name):
        try:
            return Track.objects.get(name=name)
        except Category.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)