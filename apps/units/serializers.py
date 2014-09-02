from apps.units import models
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Unit
        fields = ('id', 'name', 'status', 'desc')



