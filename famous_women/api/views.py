from rest_framework.generics import ListAPIView

from api.serializers import WomenSerializers
from women.models import Women


class WomenApiView(ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializers
