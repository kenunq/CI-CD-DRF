from rest_framework import mixins, viewsets

from SimpleApp.models import SimpleModel

from SimpleApp.serializers import SimpleModelSerizalizer

# Create your views here.


class SimpleListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = SimpleModelSerizalizer
    queryset = SimpleModel.objects.all()
