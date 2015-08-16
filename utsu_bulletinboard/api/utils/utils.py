import requests
from math import sqrt, math

from .yelp import find_yelp_posts

from .sendsms import SMS

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
	scenic_routes = []
	# MATH ALERT

	# convert to decimal for ya boy #yaboybillnye
	point_a[0] = Decimal(point_a[0])
	point_a[1] = Decimal(point_a[1])
	point_b[0] = Decimal(point_b[0])
	point_b[1] = Decimal(point_b[1])

	# distance formula
	distance = math.hypot(point_b[1] - point_a[0]), (point_b[1] - point[0]))

	y = 0
	x = 0
	# just find 5 spots for now
	interval = distance / 5
	for i in range(5):
		x = (point_a[1] + point_b[1]) / interval
		y = (point_a[0] + point_b[0]) / interval
		scenic_routes.append(find_yelp_spot(x, y))

	return order_points(scenic_routes)

def order_points(self, point_a, point_b, points):
	'''Order the points from closest to farthest in between point_a
	point_b.

	Params: []
	'''
	pass

def send_unconfirmed(self, trip_id):
	'''Send a sms to the rider(s) phone number
	when a trip is created.
	'''
	riders = User.objects.filter(
		trip_id=trip_id,
		is_customer=False)
	for rider in riders:
	    sms = SMS(rider.number)  
	    status = sms.send("A customer is waiting for your reply, a trip has been requested.")
	return status

def send_confirmed(self, user_number):
	'''Send a sms to the customers phone number
	when a trip is confirmed.
	'''
    sms = SMS(user_number)  
    status = sms.send("A rider has confirmed your trip request.")
	return status

def send_arrived(self, user_number):
	'''Send a sms to the customers phone number
	when a rider has arrived at the pickup location.
	'''
	sms = SMS(user_number)  
    status = sms.send("Your rider has arrived at your pick-up location.")
	return status
