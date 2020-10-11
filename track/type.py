from graphene_django import DjangoObjectType
from track.models import Track


class TrackType(DjangoObjectType):
    class Meta:
        model = Track  
        fields = ('id', 'name', 'file', 'cost')