import graphene
from graphene_django import DjangoObjectType
from datetime import datetime
from .models import CustomUser


class UserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = ('id', 'name', 'dob', 'email', 'profile_picture', 'location',
                  'date_joined')


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    user_by_name = graphene.Field(UserType,
                                  name=graphene.String(required=True))

    def resolve_all_users(root, info):
        return CustomUser.objects.all()

    def resolve_user_by_name(root, info, name):
        try:
            return CustomUser.objects.get(name=name)
        except CustomUser.DoesNotExist:
            return None


class CreateUserInput(graphene.InputObjectType):
    name = graphene.String()
    dob = graphene.String()
    email = graphene.String()
    location = graphene.String()
    password = graphene.String()


class CreateUser(graphene.Mutation):
    class Arguments:
        user_data = CreateUserInput(required=True)

    user = graphene.Field(UserType)

    def mutate(root, info, user_data=None):
        
        user = CustomUser.objects.create_user(name=user_data.name,
                                         email=user_data.email,
                                         password=user_data.password,
                                         location=user_data.location,
                                         dob=datetime.strptime(user_data.dob, "%m.%d.%Y"))
        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutation,
                         types=[CreateUserInput])
