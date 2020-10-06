import graphene


class Mutation(graphene.ObjectType):
    class Arguments:
        data = ""