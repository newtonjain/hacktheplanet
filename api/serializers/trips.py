from rest_framework import serializers
from address.models import Address

from bmw.models import Trip, TripStatus
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

    class Meta:
        model = Trip
        fields = ['id', 'name', 'scenic', 'trip_status',
                  'driver', 'customer', 'start', 'end', 'price']

    def validate_trip_status(self, value):
        '''Change status based on input and the last known status of the trip.

        None -> REQUESTED
        REQUESTED -> PICKING UP
        PICKING UP -> DRIVING
        DRIVING -> FINISHED
        '''
        status_name = value
        if status_name not in TripStatus.STATUSES:
            raise serializers.ValidationError('Not a valid status name.')

        if not self.instance:
            return

        if status_name is 'REQUESTED' and self.instance.trip_status.name is None:
            self.instance.status = TripStatus.objects.get(name='REQUESTED')
        if status_name is 'PICKING UP' and self.instance.status.name is 'REQUESTED':
            self.instance.status = TripStatus.objects.get(name='PICKING UP')
        if status_name is 'DRIVING' and self.instance.status.name is 'PICKING UP':
            self.instance.status = TripStatus.objects.get(name='DRIVING')
        if status_name is 'FINISHED' and self.instance.status.name is 'DRIVING':
            self.instance.status = TripStatus.objects.get(name='FINISHED')
        self.instance.save(fields=['status_id'])
        return value

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
