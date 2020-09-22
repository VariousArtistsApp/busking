import album.schema
import artist.schema
import track.schema
import user.schema
import label.schema
import graphene
from graphene_django.debug import DjangoDebug


class Query(
    album.schema.Query,
    track.schema.Query,
    label.schema.Query,
    user.schema.Query,
    artist.schema.Query,
    graphene.ObjectType,
):
    debug = graphene.Field(DjangoDebug, name="_debug")


class Mutation(
    user.schema.Mutation,
):
    debug = graphene.Field(DjangoDebug, name="_debug")


schema = graphene.Schema(query=Query, mutation=Mutation)
