# coding=utf-8

import graphene
from core import schema

class Query(schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
