
from django.db import models

from address.models import AddressField
from ._common import Trip

class Location(models.Model):
	location = AddressField(blank=True, null=True)
	trip = models.ForeignKey(Trip)
