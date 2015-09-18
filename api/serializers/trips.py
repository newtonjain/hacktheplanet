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
    status = serializers.CharField(source='trip_status.name')
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

        if self.instance.trip_status.name is None:
            self.instance.status = TripStatus.objects.get(name='REQUESTED')
        if status_name is 'REQUESTED':
            self.instance.status = TripStatus.objects.get(name='PICKING UP')
        if status_name is 'PICKING UP':
            self.instance.status = TripStatus.objects.get(name='DRIVING')
        if status_name is 'DRIVING':
            self.instance.status = TripStatus.objects.get(name='FINISIHED')
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
        trip.save()
        # for route_data in routes_data:
        #     start_aadr = Address.objects.create(**route_data['start'])
        #     end_aadr = Address.objects.create(**route_data['end'])
        return trip

    # def validate_status(self, value):
    #     if self.instance:
    #         print(self.instance.users)
    #         customer = self.instance.users.filter(is_customer=True).first()
    #         new_status = value
    #         if (self.instance.status == 'unconfirmed' and
    #                 new_status == 'confirmed'):
    #             send_confirmed(user_number=customer.phone_number)
    #         if (self.instance.status == 'confirmed' and
    #                 new_status == 'arrived'):
    #             send_arrived(user_number=customer.phone_number)
    #     return value
