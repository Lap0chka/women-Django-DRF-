from django.utils.text import slugify
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from api.serializers import WomenSerializers
from women.models import Women, Categories


class WomenApiView(ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializers


class WomenApiUpdate(UpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializers


class WomenApiDetail(RetrieveUpdateDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializers
