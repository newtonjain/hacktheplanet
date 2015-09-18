from rest_framework import serializers

from address.models import Address


class AddressCreateDetailSerializer(serializers.ModelSerializer):
    latitude = serializers.CharField()
    longitude = serializers.CharField()

    class Meta:
        model = Address
        fields = ['id', 'latitude', 'longitude']
