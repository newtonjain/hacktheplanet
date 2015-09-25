from math import radians, cos, sin, asin, sqrt

from django.db import models

from bmw.generics import ArchivableModel
from address.models import AddressField, Address
from ._common import TripStatus
from ._customer import Customer
from ._driver import Driver

from api.utils.utils import (
    send_confirmed,
    send_arrived
)


class Trip(ArchivableModel):
    name = models.CharField(blank=True, null=True,
                            max_length=100)
    scenic = models.BooleanField(blank=True, default=False)

    # relationships
    driver = models.ForeignKey(Driver, related_name='driver_trips', null=True)
    customer = models.ForeignKey(Customer, related_name='customer_trips', null=True)
    start = AddressField(
        blank=True,
        null=True,
        related_name='starting_trips')
    end = AddressField(
        blank=True,
        null=True,
        related_name='ending_trips')
    trip_status = models.ForeignKey(TripStatus, blank=True, null=True)
    scenic_locations = models.ManyToManyField(Address)

    @property
    def price(self):
        '''Returns the price of the trip based on the distance
        of the trip.
        '''
        if self.start is None or self.end is None:
            return 0
        # convert decimal degrees to radians
        lon1, lat1, lon2, lat2 = map(radians, [
            float(self.start.longitude),
            float(self.start.latitude),
            float(self.end.longitude),
            float(self.end.latitude)])
        # haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        km = 6367 * c
        return km * 200

    def change_status(self, new_status):
        '''Change the status based on the status coming in and
        the previous status.
        '''
        if new_status == 'PICKING UP' and self.trip_status.name == 'REQUESTED':
            print('sending confirmed text')
            send_confirmed(self.customer.phone_number)
            self.trip_status = TripStatus.objects.get(name='PICKING UP')
        if new_status == 'ARRIVED' and self.trip_status.name == 'PICKING UP':
            self.trip_status = TripStatus.objects.get(name='ARRIVED')
            print('send arrived text')
            send_arrived(self.customer.phone_number)
        if new_status == 'FINISHED' and self.trip_status.name == 'ARRIVED':
            self.trip_status = TripStatus.objects.get(name='FINISHED')

        self.save()
