from rest_framework import serializers

from address.models import Address


class AddressCreateDetailSerializer(serializers.ModelSerializer):
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()

    class Meta:
        model = Address
        fields = ['latitude', 'longitude']
