from datetime import datetime

from django.db import models
from django.utils import timezone

from users.models import User


class Trip(models.Model):
	# real fields
	scenic = models.BooleanField(blank=True, default=False)
	start_ts = models.DateTimeField(blank=True, default=timezone.now)
	status = models.CharField(
		blank=True, 
		default='unconfirmed',
		max_length=200)

	# relationships
	customer = models.ForeignKey(User, related_name='customer_trips')
	rider = models.ForeignKey(User, related_name='rider_trips')
