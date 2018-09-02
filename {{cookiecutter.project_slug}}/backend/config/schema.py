import graphene
from graphene_django.debug import DjangoDebug

import apps.users.schema


class Query(apps.users.schema.Query, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='__debug')


class Mutation(apps.users.schema.Mutation, graphene.ObjectType):
    ...


schema = graphene.Schema(query=Query, mutation=Mutation)
