import graphene
from user.models import CustomUser
from .type import UserType
from .mutations import CreateUser, CreateLabelUser, CreateArtistUser


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



class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    create_label_user = CreateLabelUser.Field()
    create_artist_user = CreateArtistUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
