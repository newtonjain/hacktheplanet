from datetime import datetime

from django.db import models
from django.utils import timezone


class Trip(models.Model):
	# real fields
	scenic = models.BooleanField(blank=True, default=False)
	start_ts = models.DateTimeField(blank=True, default=timezone.now)
	status = models.CharField(
		blank=True, 
		default='unconfirmed',
		max_length=200)

	def send_unconfirmed(self):
		'''Send a sms to the rider(s) phone number
		when a trip is created.
		'''
		for user in self.riders.all():
			user.send_text(status='unconfirmed')
		return

	def send_confirmed(self):
		'''Send a sms to the customers phone number
		when a trip is confirmed.
		'''
		self.customer.send_text(status='confirmed')
		return

	def send_arrived(self):
		'''Send a sms to the customers phone number
		when a rider has arrived at the pickup location.
		'''
		self.customer.send_text(status='arrived')
		return