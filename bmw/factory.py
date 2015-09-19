from datetime import datetime
from pytz import timezone
import factory
from faker import Faker
from bmw.models import *
import random
import math
from address.models import Address

fake = Faker()

today = datetime(2015, 1, 1)
today = today.replace(tzinfo=timezone('UTC'))


class CustomerFactory(factory.Factory):

    class Meta:
        model = Customer

    name = fake.first_name()
    username = factory.Sequence(lambda n: 'customer%s' % n)
    email = fake.email()
    is_active = True
    description = fake.paragraphs(nb=2)


class DriverFactory(factory.Factory):

    class Meta:
        model = Driver

    name = fake.first_name()
    username = factory.Sequence(lambda n: 'driver%s' % n)
    email = fake.email()
    bike_model = 'BMW G 650 GS'
    is_active = True
    description = fake.paragraphs(nb=2)


class TripFactory(factory.Factory):

    class Meta:
        model = Trip

    name = fake.first_name()
    scenic = False
    start = None
    end = None
    trip_status = None


def make_objects():
    drivers = DriverFactory.build_batch(10)
    for driver in drivers:
        driver.save()
    customers = CustomerFactory.build_batch(10)
    for customer in customers:
        customer.save()
    trips = TripFactory.build_batch(10)
    for event in trips:
        event.driver = Driver.objects.order_by('?').first()
        event.customer = Customer.objects.order_by('?').first()
        event.trip_status = TripStatus.objects.order_by('?').first()
        # create some random addresses
        radius = 100
        radiusInDegrees = radius / 111300
        r = radiusInDegrees
        x0 = 37.788081
        y0 = -122.34375
        u = float(random.uniform(0.0, 1.0))
        v = float(random.uniform(0.0, 1.0))
        w = r * math.sqrt(u)
        t = 2 * math.pi * v
        x = w * math.cos(t)
        y = w * math.sin(t)
        xLat = x + x0
        yLong = y + y0
        event.start = Address.objects.create(
            latitude=xLat,
            longitude=yLong)
        u = float(random.uniform(0.0, 1.0))
        v = float(random.uniform(0.0, 1.0))
        w = r * math.sqrt(u)
        t = 2 * math.pi * v
        x = w * math.cos(t)
        y = w * math.sin(t)
        xLat = x + x0
        yLong = y + y0
        event.end = Address.objects.create(
            latitude=xLat,
            longitude=yLong)
        event.save()
