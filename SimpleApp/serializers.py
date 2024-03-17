from rest_framework import serializers

from .models import SimpleModel


class SimpleModelSerizalizer(serializers.ModelSerializer):
    class Meta:
        model = SimpleModel
        fields = "__all__"
