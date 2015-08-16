from rest_framework import serializers

from address.models import AddressField
from api.models import Trip, Location
from users.models import User


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = AddressField
        fields = ['id', 'latitude', 'longitude']


class LocationSerializer(serializers.ModelSerializer):
    start = AddressSerializer()
    end = AddressSerializer()

    class Meta:
        model = Location
        fields = ['id', 'start', 'end']


class TripSerializer(serializers.ModelSerializer):
    locations = LocationSerializer(many=True)
    status = serializers.CharField(required=False)

    class Meta:
        model = Trip
        fields = ['id', 'locations', 'scenic', 'start_ts', 'status',
        'users']

    def update(self, instance, validated_data):
        riders = validated_data.get('riders')
        if riders and len(riders) == 1:
            instance.status = 'confirmed'
        return instance.save(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    trips = TripSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'photo', 'username', 'is_customer', 'phone_number',
        'description', 'trips', 'interests']