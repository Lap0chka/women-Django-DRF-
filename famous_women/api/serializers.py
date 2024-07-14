from django.utils.text import slugify
from rest_framework.serializers import ModelSerializer

from women.models import Women


class WomenSerializers(ModelSerializer):
    class Meta:
        model = Women
        fields = '__all__'
        read_only_fields = ['slug', 'time_create', 'time_update']

    def create(self, validated_data):
        categories = validated_data.pop('cat', [])
        women_instance = super().create(validated_data)
        women_instance.cat.set(categories)
        return women_instance
