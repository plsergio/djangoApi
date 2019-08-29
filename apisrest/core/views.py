#coding=utf-8


from .models import Music, Chave, Product
from .serializers import MusicSerializer, ChaveSerializer, ProductSerializer
from rest_framework import generics

class MusicList(generics.ListCreateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

class ChaveList(generics.ListCreateAPIView):
    queryset = Chave.objects.all()
    serializer_class = ChaveSerializer

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
