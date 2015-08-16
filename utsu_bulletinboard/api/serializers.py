from rest_framework import serializers

from address.models import AddressField
from api.models import Trip, Location
from users.models import User


class AddressSerializer(serializers.Serializer):

    class Meta:
        model = AddressField
        fields = ['latitude', 'longitude']


class LocationSerializer(serializers.Serializer):
    start = AddressSerializer()
    end = AddressSerializer()

    class Meta:
        model = Location
        fields = ['id', 'start', 'end']


class TripSerializer(serializers.Serializer):
    locations = LocationSerializer(many=True)
    status = serializers.CharField(required=False)
    # riders = serializers.SerializerMethodField('get_riders')

    class Meta:
        model = Trip
        fields = ['locations', 'scenic', 'start_ts', 'status',
        'riders']

    def update(self, instance, validated_data):
        riders = validated_data.get('riders')
        if riders and len(riders) == 1:
            instance.status = 'confirmed'
        return instance.save(**validated_data)

    # def get_riders(self, trip):
    #     qs = User.objects.filter(is_customer=False, trip=trip)
    #     serializer = UserSerializer(
    #         instance=qs, 
    #         many=True, 
    #         required=False)
    #     return serializer.data


class UserSerializer(serializers.Serializer):
    trips = TripSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'photo', 'name', 'type_of_user', 'phone_number',
        'description', 'trips']