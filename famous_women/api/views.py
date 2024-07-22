from django.utils.text import slugify
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.serializers import WomenSerializers
from women.models import Women, Categories


class WomenViewSet(ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializers



