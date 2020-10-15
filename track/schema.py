import graphene

from track.models import Track

from .mutations import CreateTrack
from .type import TrackType


class Query(graphene.ObjectType):
    all_tracks = graphene.List(TrackType)
    track_by_name = graphene.Field(TrackType,
                                   name=graphene.String(required=True))

    def resolve_all_tracks(root, info):
        return Track.objects.all()

    def resolve_track_by_name(root, info, name):
        try:
            return Track.objects.get(name=name)
        except Track.DoesNotExist:
            return None


class Mutation(graphene.ObjectType):
    create_track = CreateTrack.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
