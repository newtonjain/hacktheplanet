from rest_framework import serializers

from address.models import Address


class AddressCreateDetailSerializer(serializers.ModelSerializer):
    latitude = serializers.IntegerField()
    longitude = serializers.IntegerField()

    class Meta:
        model = Address
        fields = ['id', 'latitude', 'longitude']
