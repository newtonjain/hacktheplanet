from rest_framework import serializers

from address.models import Address
from api.models import Trip, Route
from users.models import User

from api.utils.utils import scenic_trip_builder
from api.utils.utils import (
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
    trip = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Route
        fields = ['id', 'name', 'start', 'end', 'trip']


class UserSerializer(serializers.ModelSerializer):
    trips = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'photo', 'username',
        'first_name', 'is_customer', 'phone_number',
        'description', 'trips', 'interests']


class TripSerializer(serializers.ModelSerializer):
    routes = RouteSerializer(many=True)
    status = serializers.CharField(required=False)
    start_ts = serializers.DateTimeField(required=False)
    users = UserSerializer(
        many=True)

    class Meta:
        model = Trip
        fields = ['id', 'routes', 'scenic', 'start_ts', 'status',
        'users']

    def create(self, validated_data):
        # get scenic Routes on the way to point B,
        # make the Route objects (attached trips to them),
        print(validated_data)
        if validated_data.get('scenic'):
            locations = validated_data['routes']
            starting_point = [locations['start']['latitude'],
                locations['start']['latitude']]
            ending_point = [locations['end']['latitude'],
                locations['end']['latitude'] ]
            scenic_trip_builder(starting_point, ending_point)

        routes_data = validated_data.pop('routes')
        trip = Trip.objects.create(**validated_data)
        for route_data in routes_data:
            start_aadr = Address.objects.create(**route_data['start'])
            end_aadr = Address.objects.create(**route_data['end'])
        Route.objects.create(start=start_aadr, end=end_aadr, trip=trip)
        return trip

    # def update (self, instance, validated_data):
    #     # customer = instance.users.filter(is_customer=True).first()
    #     # if (instance.status == 'unconfirmed' and
    #     #     validated_data.get('status', None) == 'confirmed'):
    #     #     send_confirmed(user_number=customer.phone_number)
    #     # if (instance.status == 'confirmed' and
    #     #     validated_data.get('status', None) == 'arrived'):
    #     #     send_arrived(user_number=customer.phone_number)
    #     #patching users
    #     print(validated_data)
    #     user_ids = validated_data.get('users')
    #     print(user_ids)
    #     instance.users = User.objects.filter(id__in=user_ids)
    #     instance.save()
    #     return instance
