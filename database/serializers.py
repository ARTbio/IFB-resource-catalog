from rest_framework import serializers

from database import models


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Service
        fields = ('name', 'credit', 'scope', 'description')
