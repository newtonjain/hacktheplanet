from rest_framework import serializers
from address.models import Address

from bmw.models import Trip
from api.serializers import addresses

# from api.utils.utils import scenic_trip_builder
# from api.utils.utils import (
#    send_arrived,
#    send_confirmed
# )


class TripSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField('trip_status')
    start = addresses.AddressCreateDetailSerializer(source='start')
    end = addresses.AddressCreateDetailSerializer(source='end')

    class Meta:
        model = Trip
        fields = ['id', 'name', 'scenic', 'start_ts', 'status',
                  'driver_id', 'customer_id', 'start', 'end']
        read_only = ['status']

    def trip_status(self, instance):
        return instance.trip_status.name

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
