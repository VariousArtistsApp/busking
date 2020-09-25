from graphene_django import DjangoObjectType
from user.models import CustomUser


class UserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = ('id', 'name', 'dob', 'email', 'profile_picture', 'location',
                  'date_joined')