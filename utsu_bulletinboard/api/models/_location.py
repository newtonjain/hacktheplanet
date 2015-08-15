
from django.db import models

from address.models import AddressField
from ._trip import Trip

class Location(models.Model):
	start = AddressField(blank=True, null=True, 
		related_name='start_locations')
	end = AddressField(blank=True, null=True, 
		related_name='end_locations')
	trip = models.ForeignKey(Trip, blank=True,
		related_name='locations')
