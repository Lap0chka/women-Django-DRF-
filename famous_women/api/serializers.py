from rest_framework.serializers import ModelSerializer

from women.models import Women


class WomenSerializers(ModelSerializer):
    class Meta:
        model = Women
        fields = '__all__'
