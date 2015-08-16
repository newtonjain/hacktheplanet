from datetime import datetime

from django.db import models
from django.utils import timezone


class Trip(models.Model):
	# real fields
	scenic = models.BooleanField(blank=True, default=False)
	start_ts = models.DateTimeField(blank=True, null=True, default=timezone.now)
	status = models.CharField(
		blank=True, 
		default='unconfirmed',
		max_length=200)
