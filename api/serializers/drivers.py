from rest_framework import serializers
from api.serializers import addresses

from bmw.models import Driver


class DriverSerializer(serializers.ModelSerializer):
    location = addresses.AddressCreateDetailSerializer()

    class Meta:
        model = Driver
        fields = ['id', 'username', 'name', 'email', 'description',
                  'bike_model', 'location']
        read_only = ['location', 'bike_model']
