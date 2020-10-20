from datetime import datetime

import graphene

from artist.models import Artist
from label.models import Label
from user.models import CustomUser

from .type import UserType


def create_user(data):
    return CustomUser.objects.create_user(name=data.name,
                                          email=data.email,
                                          password=data.password,
                                          location=data.location,
                                          dob=datetime.strptime(data.dob, "%d.%m.%Y"))  # noqa E501


class CreateUserInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    dob = graphene.String(required=True)
    email = graphene.String(required=True)
    location = graphene.String(required=True)
    password = graphene.String(required=True)
    labelName = graphene.String()
    artistName = graphene.String()


class CreateUser(graphene.Mutation):
    class Arguments:
        data = CreateUserInput(required=True)

    user = graphene.Field(UserType)

    def mutate(root, info, data=None):
        user = create_user(data)
        if data.artistName:
            artist = Artist.objects.create(name=data.artistName)
            user.artist_profile = artist
            user.save()
        elif data.labelName:
            label = Label.objects.create(name=data.labelName, email=data.email)
            user.label_profile = label
            user.save()
        return CreateUser(user=user)
