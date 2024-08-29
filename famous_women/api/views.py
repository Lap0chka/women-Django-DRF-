
from rest_framework.viewsets import ModelViewSet

from api.serializers import WomenSerializers
from women.models import Women, Categories


class WomenViewSet(ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializers



