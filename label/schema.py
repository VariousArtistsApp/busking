import graphene
from graphene_django import DjangoObjectType
from user.type  import UserType
from .models import Label


class LabelType(DjangoObjectType):
    class Meta:
        model = Label
        fields = '__all__'


class Query(graphene.ObjectType):
    all_labels = graphene.List(LabelType)
    label_by_name = graphene.Field(LabelType, name=graphene.String(required=True))

    def resolve_all_labels(root, info):
        return Label.objects.all()

    def resolve_label_by_name(root, info, name):
        try:
            return Label.objects.get(name=name)
        except Category.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)