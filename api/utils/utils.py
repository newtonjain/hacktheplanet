import requests
from math import sqrt

# from .yelp import find_yelp_posts

from .sendsms import SMS

# from .models import Route, Trip
# from users.model import User


def distance(point_m, point_n):
    d0 = point_n[0] - point_m[0]
    d1 = point_n[1] - point_m[0]
    return sqrt(d0**2 + d1**2)


def scenic_trip_builder(point_a, point_b):
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
    distance = math.hypot((point_b[1] - point_a[0]), (point_b[1] - point[0]))

    y = 0
    x = 0
    # just find 5 spots for now
    interval = distance / 5
    for i in range(5):
        x = (point_a[1] + point_b[1]) / interval
        y = (point_a[0] + point_b[0]) / interval
        # scenic_routes.append(find_yelp_spot(x, y))

    return order_points(scenic_routes)


def order_points(points):
    """ Given an array of coordinate pairs
    i.e. [[x1, y1], [x2, y2], [x3, y3] , ... ]
    IMPORTANT: first and last coordinates are assumed endpoints
    Returns the same format in the optimum route

    [FOR TESTING]:
    PAIR1 = [[3, 3], [1, 2], [0, 0], [2, -1], [3, 4], [5, 5]]
    PAIR2 = [[1, 1], [5, 3], [8, 2], [6, 7], [2, 5], [-5, -7], [4, 4], [3, 2]]
    PAIR3 = [[0, 0], [9, 1], [5, 5], [3, 1], [4, 2], [0, 13], [8, 5], [2, 10]]
    """
    print("\n<PAIR value='" + str(points) + "'>")
    points = points[::-1]
    response = []
    response.append(points.pop(len(points) - 1))

    while len(points) > 1:
        print("\nRemaining Points: \n" + str(points) + "\n")
        distances = []

        for i in range(len(points) - 1):
            print(str(points[0])+" to "+str(points[i+1])+" is "+str(distance(points[0], points[i+1])))
            distances.append(distance(points[0], points[i+1]))

        response.append(points.pop(0))
        shortest = distances.index(min(distances))
        print("\nClosest Point: " + str(points[shortest]))
        if shortest != 0:
            points.append(points[0])
            points[0] = points[shortest]
            points.pop(shortest)


    response.append(points.pop(0))
    response.append(response.pop(0))
    response = response[::-1]
    print("\n<RESPONSE>" + str(response) + "</RESPONSE>\n</PAIR>")

    # lists all distance relationships
    """
    for i in range(len(points)):
        for j in range(len(points)):
            if i != j and j > i:
                print(str(points[i])+" to "+str(points[j])+" is "+str(distance(points[i], points[j])))
    """
    return response


def send_unconfirmed(user_number):
    '''Send a sms to the rider(s) phone number
    when a trip is created.
    '''
    status = None
    if user_number:
        sms = SMS(user_number)
        status = sms.send("A rider has requested a ride.")
    return status


def send_confirmed(user_number):
    '''Send a sms to the customers phone number
    when a trip is confirmed.
    '''
    status = None
    if user_number:
        sms = SMS(user_number)
        status = sms.send("A rider has confirmed your trip request.")
    return status


def send_arrived(user_number):
    '''Send a sms to the customers phone number
    when a rider has arrived at the pickup location.
    '''
    status = None
    if user_number:
        sms = SMS(user_number)
        status = sms.send("Your rider has arrived at your pick-up location.")
    return status
