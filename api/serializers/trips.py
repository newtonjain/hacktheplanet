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
    status = serializers.CharField(source='trip_status.name', required=False)
    start = addresses.AddressCreateDetailSerializer(source='start')
    end = addresses.AddressCreateDetailSerializer(source='end')
    price = serializers.IntegerField()

    class Meta:
        model = Trip
        fields = ['id', 'name', 'scenic', 'start_ts', 'trip_status',
                  'driver_id', 'customer_id', 'start', 'end']
        read_only = ['status']

    def validate_status_name(self, value):
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
        # get scenic Trips on the way to point B,
        # if validated_data.get('scenic'):
        #     locations = validated_data.get('routes')[0]
        #     starting_point = [locations['start']['latitude'],
        #                       locations['start']['latitude']]
        #     ending_point = [locations['end']['latitude'],
        #                     locations['end']['latitude']]
        #     scenic_trip_builder(starting_point, ending_point)

        start_data = validated_data.pop('start')
        start_address = Address(**start_data)
        end_data = validated_data.pop('end')
        end_address = Address(**end_data)
        trip = Trip.objects.create(**validated_data)
        trip.start = start_address
        trip.end = end_address
        trip.trip_status = TripStatus.objects.get(name='REQUESTED')
        trip.save()
        # for route_data in routes_data:
        #     start_aadr = Address.objects.create(**route_data['start'])
        #     end_aadr = Address.objects.create(**route_data['end'])
        return trip

    def validate_scenic(self, value):
        '''If True, create a scenic journey, if not, do A to B.'''
        is_scenic = value
        pass
        # if is_scenic:

