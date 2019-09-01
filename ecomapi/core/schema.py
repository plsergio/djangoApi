# coding=utf-8

from django.contrib.auth import get_user_model

import graphene
from graphene_django import DjangoObjectType

from .models import Produto


import graphene
from graphene_django import DjangoObjectType

from .models import Produto

class ProdutoType(DjangoObjectType):
    class Meta:
        model = Produto


class Query(graphene.ObjectType):
    produtos = graphene.List(ProdutoType)

    def resolve_produtos(self, info, **kwargs):
        return Produto.objects.all()
