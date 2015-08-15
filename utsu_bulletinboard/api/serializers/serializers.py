from rest_framework import serializers

from address.models import AddressField
from api.models import Trip, Location
from users.models import User


class TripSerializer(serializers.Serializer):
    locations = LocationSerializer(many=True)
    riders = UserSerializer(many=True, source='rider')
    status = serializers.CharField(required=False)

    class Meta:
        model = Trip
        fields = ['customer', 'locations', 'riders', 'scenic',
        'start_ts', 'status']

    def update(self, instance, validated_data):
        riders = validated_data.get('riders')
        if riders and len(riders) == 1:
            instance.status = 'confirmed'
            instance.save()
        return instance


class UserSerializer(serializers.Serializer):
    # make all other fields non-required

    class Meta:
        model = User
        fields = ['id', 'photo', 'name', 'type_of_user', 'phone_number',
        'description', 'interets']



class LocationSerializer(serializers.Serializer):

    class Meta:
        model = Location
        fields = ['id', 'start', 'end']


class AddressSerializer(serializers.Serializer):

    class Meta:
        model = AddressField
        fields = ['latitude', 'longitude']