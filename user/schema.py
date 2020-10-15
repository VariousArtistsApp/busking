import graphene

from busking_auth.utils import decode_token
from user.models import CustomUser

from .mutations import CreateUser
from .type import UserType


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    user_by_name = graphene.Field(UserType,
                                  name=graphene.String(required=True))
    me = graphene.Field(UserType)

    def resolve_all_users(root, info):
        return CustomUser.objects.all()

    def resolve_user_by_name(root, info, name):
        try:
            return CustomUser.objects.get(name=name)
        except CustomUser.DoesNotExist:
            return None

    def resolve_me(root, info):
        user = decode_token(info.context.COOKIES.get('token'))
        return CustomUser.objects.get(id=user['user'])


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
