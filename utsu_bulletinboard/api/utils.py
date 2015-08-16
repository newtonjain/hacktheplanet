import requests


from api.models import Location, Trip
from users.model import User

def scenic_trip_builder(self, point_a, point_b):
	'''Builds a scenic route to point_b using Yelps api.

	Limit of 4 locations will be attached to a trip.

	Params:
		point_a: Location data of the starting point
		Type: List
		Format: [latitude, longitude]

		point_b: Location data of the destination
		Type: List
		Format: [latitude, longitude]

	'''
	print(trip)
	# iterate 20% of the way (5 times for each trip)
	pass


def send_unconfirmed(self, trip):
	'''Send a sms to the rider(s) phone number
	when a trip is created.
	'''
	riders = User.objects.filter(
		trip_id=trip.id,
		is_customer=False)
	for rider in riders:
		send_text(user=rider, status='unconfirmed')
	return
	
def send_confirmed(self, user):
	'''Send a sms to the customers phone number
	when a trip is confirmed.
	'''
	send_text(user=user, status='confirmed')
	return

def send_arrived(self, trip_id):
	'''Send a sms to the customers phone number
	when a rider has arrived at the pickup location.
	'''
	send_text(user=user, status='arrived')
	return