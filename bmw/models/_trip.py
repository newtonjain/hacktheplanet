from math import radians, cos, sin, asin, sqrt

from django.db import models
from django.utils import timezone

from bmw.generics import ArchivableModel
from address.models import AddressField, Address
from ._common import TripStatus
from ._customer import Customer
from ._driver import Driver


class Trip(ArchivableModel):
    name = models.CharField(blank=True, null=True,
                            max_length=100)
    scenic = models.BooleanField(blank=True, default=False)
    start_ts = models.DateTimeField(blank=True, null=True, default=timezone.now)

    # relationships
    driver = models.ForeignKey(Driver, related_name='driver_trips')
    customer = models.ForeignKey(Customer, related_name='customer_trips')
    start = AddressField(
        blank=True,
        null=True,
        related_name='starting_trips')
    end = AddressField(
        blank=True,
        null=True,
        related_name='ending_trips')
    trip_status = models.ForeignKey(TripStatus)

    @property
    def price(self):
        '''Returns the price of the trip based on the distance
        of the trip.
        '''
        if self.start is None or self.end is None:
            return 0
        # convert decimal degrees to radians
        lon1, lat1, lon2, lat2 = map(radians, [
            self.start.longitude,
            self.start.latitude,
            self.end.longitude,
            self.end.latitude])
        # haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        km = 6367 * c
        return km

    def trip_builder(self):
        '''Builds a scenic trip based on the start and end points.'''
        pass
