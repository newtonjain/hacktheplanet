from rest_framework import serializers
from address.models import Address

from bmw.models import Trip, TripStatus, Customer, Driver
from api.serializers import addresses

# from api.utils.utils import scenic_trip_builder
# from api.utils.utils import (
#    send_arrived,
#    send_confirmed
# )


class TripSerializer(serializers.ModelSerializer):
    trip_status = serializers.CharField(
        source='trip_status.name',
        required=False,
        allow_null=True)
    start = addresses.AddressCreateDetailSerializer()
    end = addresses.AddressCreateDetailSerializer()
    price = serializers.IntegerField(read_only=True)
    driver_id = serializers.PrimaryKeyRelatedField(
        queryset=Driver.objects.all())
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all())

    class Meta:
        model = Trip
        fields = ['id', 'name', 'scenic', 'trip_status',
                  'driver_id', 'customer_id', 'start', 'end', 'price']

    def update(self, instance, validated_data):
        '''Change status based on input and the last known status of the trip.

        None -> REQUESTED
        REQUESTED -> PICKING UP
        PICKING UP -> DRIVING
        DRIVING -> FINISHED
        '''
        status_name = validated_data.get('trip_status')
        status_name = status_name.get('name')
        if status_name not in TripStatus.objects.all().values_list('name', flat=True):
            raise serializers.ValidationError('Not a valid status name.')
        if status_name == 'PICKING UP' and instance.trip_status.name == 'REQUESTED':
            instance.trip_status = TripStatus.objects.get(name='PICKING UP')
        if status_name == 'DRIVING' and instance.trip_status.name == 'PICKING UP':
            instance.trip_status = TripStatus.objects.get(name='DRIVING')
        if status_name == 'FINISHED' and instance.trip_status.name == 'DRIVING':
            instance.trip_status = TripStatus.objects.get(name='FINISHED')
        instance.save()
        return instance

    def create(self, validated_data):
        start_data = validated_data.pop('start')
        start_address = Address.objects.create(**start_data)
        end_data = validated_data.pop('end')
        end_address = Address.objects.create(**end_data)
        trip = Trip.objects.create(**validated_data)
        if trip.scenic:
            trip.trip_builder()
        trip.start = start_address
        trip.end = end_address
        trip.trip_status = TripStatus.objects.get(name='REQUESTED')
        trip.save()
        return trip
