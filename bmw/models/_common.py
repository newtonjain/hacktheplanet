from django.db import models

from bmw.generics import ArchivableModel


class TripStatus(ArchivableModel):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    class Meta:
        db_table = 'trip_statuses'
