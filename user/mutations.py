import graphene
from label.models import Label
from label.schema import LabelType
from artist.models import Artist
from artist.schema import ArtistType
from .type import UserType
from user.models import CustomUser
from datetime import datetime


def create_user(data):
    return CustomUser.objects.create_user(name=data.name,
                                          email=data.email,
                                          password=data.password,
                                          location=data.location,
                                          dob=datetime.strptime(data.dob, "%m.%d.%Y"))


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
