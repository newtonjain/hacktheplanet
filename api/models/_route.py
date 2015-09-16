
from django.db import models

from address.models import Address
from ._trip import Trip


class Route(models.Model):
    name = models.CharField(blank=True, null=True,
                            max_length=100)
    start = models.ForeignKey(
        Address,
        blank=True,
        null=True,
        related_name='starting_addresses')
    end = models.ForeignKey(
        Address,
        blank=True,
        null=True,
        related_name='ending_addresses')
    trip = models.ForeignKey(Trip, blank=True,
                             related_name='routes')
