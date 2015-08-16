import requests

from math import sqrt

# from .models import Route, Trip
# from users.model import User

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
	# MATH ALERT
	point_a[0] = Decimal(point_a[0])
	point_a[1] = Decimal(point_a[1])
	point_b[0] = Decimal(point_b[0])
	point_b[1] = Decimal(point_b[1])
	#find five points along the way from point a to point b
	distance = sqrt(
		(point_b[1] - point_a[0])**2 + (point_b[1] - point[0])**2
	)

	y = 0
	x = 0
	interval = distance / 5
	for i in range(5):
		y = (point_a[0] + point_a[1]) - x
		sqrt(
			(point_b[1] - y)**2 + (point_b[0] - x)**2
		)
		pass




	pass

# def 

def order_points(self, point_a, point_b, points):
	'''Order the points from closest to farthest in between point_a
	point_b.
	'''
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