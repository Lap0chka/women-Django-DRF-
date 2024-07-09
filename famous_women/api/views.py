from django.utils.text import slugify
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from api.serializers import WomenSerializers
from women.models import Women, Categories


class WomenApiView(ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializers

    # def post(self, request):
    #     serialized = WomenSerializers(data=request.data)
    #     serialized.is_valid(raise_exception=True)
    #
    #     title = request.data['title']
    #     slug = slugify(title) if 'slug' not in request.data else request.data['slug']
    #     cat_ids = request.data.get('cat')
    #
    #     post_new = Women()
    #     post_new.save()
    #     categories = Categories.objects.filter(id__in=cat_ids)
    #     post_new.cat.set(categories)
    #
    #     return Response({'posts': WomenSerializers(post_new).data})
