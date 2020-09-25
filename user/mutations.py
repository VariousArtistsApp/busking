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
    name = graphene.String()
    dob = graphene.String()
    email = graphene.String()
    location = graphene.String()
    password = graphene.String()


class CreateArtistUserInput(CreateUserInput, graphene.InputObjectType):
    artistName = graphene.String()


class CreateLabelUserInput(CreateUserInput, graphene.InputObjectType):
    labelName = graphene.String()


class CreateUser(graphene.Mutation):
    class Arguments:
        data = CreateUserInput(required=True)

    user = graphene.Field(UserType)

    def mutate(root, info, data=None):
        user = create_user(data)
        return CreateUser(user=user)


class CreateArtistUser(graphene.Mutation):
    class Arguments:
        data = CreateArtistUserInput(required=True)

    user = graphene.Field(UserType)
    artist = graphene.Field(ArtistType)

    def mutate(root, info, data=None):
        user = create_user(data)
        artist = Artist.objects.create(name=data.artistName)
        user.artist_profile = artist
        user.save()
        return CreateArtistUser(user=user, artist=artist)


class CreateLabelUser(graphene.Mutation):
    class Arguments:
        data = CreateLabelUserInput(required=True)

    user = graphene.Field(UserType)
    label = graphene.Field(LabelType)

    def mutate(root, info, data=None):
        user = create_user(data)
        label = Label.objects.create(name=data.labelName, email=data.email)
        user.label_profile = label
        user.save()
        return CreateLabelUser(user=user, label=label)