from rest_framework import serializers

from address.models import Address


class AddressCreateDetailSerializer(serializers.ModelSerializer):
    latitude = serializers.DecimalField(max_digits=10, decimal_places=5)
    longitude = serializers.DecimalField(max_digits=10, decimal_places=5)

    class Meta:
        model = Address
        fields = ['id', 'latitude', 'longitude']
