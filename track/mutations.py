import graphene

from .models import Track
from .type import TrackType


class CreateTrackInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    artistName = graphene.String(required=True)
    price = graphene.String(required=True)
    file = graphene.String(required=True)


class CreateTrack(graphene.Mutation):
    class Arguments:
        data = CreateTrackInput(required=True)

    track = graphene.Field(TrackType)

    def mutate(root, info, data=None):
        track = Track.objects.create(name=data.name, price=data.price,
                                     file=data.file)
        return CreateTrack(track=track)
