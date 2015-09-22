from rest_framework import serializers
from api.serializers import addresses
import random

from address.models import Address
from bmw.models import Driver


class DriverSerializer(serializers.ModelSerializer):
    location = addresses.AddressCreateDetailSerializer(required=False)

    class Meta:
        model = Driver
        fields = ['id', 'name', 'email', 'description',
                  'bike_model', 'location', 'facebook_id',
                  'phone_number', 'profile_picture_url']
        read_only = ['bike_model']

    def create(self, validated_data):
        location_data = validated_data.pop('location')
        location = Address.objects.create(**location_data)
        driver = Driver.objects.create(
            username=str(random.uniform(0.0, 1.0)),
            **validated_data
        )
        driver.location = location
        driver.save()
        return driver
