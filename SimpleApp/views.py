from rest_framework import mixins, viewsets  # noqa: EXE002

from SimpleApp.models import SimpleModel
from SimpleApp.serializers import SimpleModelSerizalizer

# Create your views here.


class SimpleListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = SimpleModelSerizalizer
    queryset = SimpleModel.objects.all()
