# coding=utf-8

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from apirest.start.serializers import UserSerializer, GroupSerializer

class UserViewerSet(viewsets.ModelViewSet):
    """
    API endpoint
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewerSet(viewsets.ModelViewSet):
    """
    API endpoint
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
