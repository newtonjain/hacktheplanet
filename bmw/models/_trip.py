from django.db import models
from django.utils import timezone

from bmw.generics import ArchivableModel
from address.models import AddressField
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
    status = models.ForeignKey(TripStatus)

    class Meta:
        db_name = 'trips'
