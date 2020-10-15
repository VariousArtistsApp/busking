import graphene
from graphene_django.debug import DjangoDebug

import album.schema
import artist.schema
import label.schema
import track.schema
import user.schema


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
    track.schema.Mutation,
    album.schema.Mutation,
):
    debug = graphene.Field(DjangoDebug, name="_debug")


schema = graphene.Schema(query=Query, mutation=Mutation)
