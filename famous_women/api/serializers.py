from rest_framework.serializers import ModelSerializer

from women.models import Women


class WomenSerializers(ModelSerializer):
    class Meta:
        model = Women
        fields = '__all__'
        read_only_fields = ['slug', 'time_create', 'time_update']
