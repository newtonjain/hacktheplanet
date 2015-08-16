from rest_framework import serializers

from address.models import Address
from api.models import Trip, Route
from users.models import User

from api.utils.utils import scenic_trip_builder
from api.utils import (
    send_arrived,
    send_confirmed,
    send_unconfirmed
    )


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ['id', 'latitude', 'longitude']


class RouteSerializer(serializers.ModelSerializer):
    start = AddressSerializer()
    end = AddressSerializer()

    class Meta:
        model = Route
        fields = ['id', 'name', 'start', 'end', 'trip']


class TripSerializer(serializers.ModelSerializer):
    routes = RouteSerializer(many=True)
    status = serializers.CharField(required=False)

    class Meta:
        model = Trip
        fields = ['id', 'routes', 'scenic', 'start_ts', 'status',
        'users']

    def create(self, validated_data):
        # get scenic Routes on the way to point B,
        # make the Route objects (attached trips to them),
        if validated_data['scenic']:
            locations = validated_data['routes']
            starting_point = [locations['start']['latitude'],
                locations['start']['latitude']]
            ending_point = [locations['end']['latitude'],
                locations['end']['latitude'] ]
            scenic_trip_builder(starting_point, ending_point)
        trip = Trip.objects.create(**validated_data)
        send_unconfirmed(trip_id=trip.id)
        return trip

    def update (self, instance, validated_data):
        customer = instance.users.filter(is_customer=True).first()
        if (instance.status == 'unconfirmed' and
            validated_data.get('status', None) == 'confirmed'):
            send_confirmed(user_id=customer.number)
        if (instance.status == 'confirmed' and
            validated_data.get('status', None) == 'arrived'):
            send_arrived(user_id=customer.number)
        return instance.save(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    trips = TripSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'photo', 'username', 'is_customer', 'phone_number',
        'description', 'trips', 'interests']
