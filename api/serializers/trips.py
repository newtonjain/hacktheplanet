from rest_framework import serializers
from address.models import Address

from bmw.models import Trip, TripStatus, Customer, Driver
from api.serializers import addresses

from api.utils.utils import (
    send_unconfirmed
)


class TripSerializer(serializers.ModelSerializer):
    trip_status = serializers.CharField(
        source='trip_status.name',
        required=False,
        allow_null=True)
    start = addresses.AddressCreateDetailSerializer()
    end = addresses.AddressCreateDetailSerializer()
    price = serializers.IntegerField(read_only=True)
    driver_facebook_id = serializers.IntegerField(
        source='driver.facebook_id')
    customer_facebook_id = serializers.IntegerField(
        source='customer.facebook_id')

    scenic_locations = addresses.AddressCreateDetailSerializer(
        many=True,
        required=False)

    class Meta:
        model = Trip
        fields = ['id', 'name', 'scenic', 'trip_status',
                  'driver_facebook_id', 'customer_facebook_id',
                  'start', 'end', 'price', 'scenic_locations']

    def update(self, instance, validated_data):
        '''Support writable nested fields.
        Supported:
        '''
        return instance

    def validate_trip_status(self, value):
        '''If trip status comes in, call change_status.'''
        trip_status = value
        if not self.instance:
            return value
        if trip_status not in TripStatus.objects.all().values_list('name', flat=True):
            raise serializers.ValidationError('Not a valid status name.')
        self.instance.change_status(new_status=trip_status)
        return trip_status

    def create(self, validated_data):
        start_data = validated_data.pop('start')
        start_address = Address.objects.create(**start_data)
        end_data = validated_data.pop('end')
        end_address = Address.objects.create(**end_data)
        driver_data = validated_data.pop('driver')
        driver_facebook_id = driver_data.get('facebook_id')
        customer_data = validated_data.pop('customer')
        customer_facebook_id = customer_data.get('facebook_id')
        driver = Driver.objects.filter(facebook_id=driver_facebook_id).first()
        customer = Customer.objects.filter(facebook_id=customer_facebook_id).first()
        if not (driver and customer):
            raise serializers.ValidationError('not valid fb ids')
        trip = Trip.objects.create(**validated_data)
        trip.driver = driver
        trip.customer = customer
        trip.start = start_address
        trip.end = end_address
        trip.trip_status = TripStatus.objects.get(name='REQUESTED')
        trip.save()
        send_unconfirmed(trip.customer.phone_number)
        if trip.scenic:
            print('creating yelp spots')
            trip.trip_builder()
        return trip
