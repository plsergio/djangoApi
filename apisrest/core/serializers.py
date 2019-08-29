#coding=utf-8

from rest_framework import serializers
from .models import Music, Chave, Product


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'

class ChaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chave
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
