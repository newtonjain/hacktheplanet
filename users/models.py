# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone

# Should be seperate but for clarity I'm putting them together to showcase our models
# from api.models import Trip

# from django.utils.translation import ugettext_lazy as _


class Trip(models.Model):
    """ Trip model """

    trip_id = models.BigIntegerField(blank=True, null=True)
	scenic = models.BooleanField(blank=True, default=False)
	start_ts = models.DateTimeField(blank=True, null=True, default=timezone.now)
	status = models.CharField(blank=True, default='unconfirmed', max_length=200)
    # Either distance or time to one-to-one with driver
    # We could reward drivers based on distance
    distance = models.BigIntergerField(blank=True, null=True)
    driver = ForeignKey(Driver)
    rider = ForeignKey(Rider)
    # Unless driver and rider could be removed and solely linked through their trip_id
    # Trip should definitely include addtional parameters

    # Why isn't this a thing?
    # def __unicode__(self):
    #     return some machine-readble shit


class User(model.Model):
    """ [Abstract] User model """

    class Meta:
        abstract = True

    name = models.CharField(blank=True, max_length=100)
    phone_number = models.BigIntegerField(blank=True, null=True)

    def __unicode__(self):
        """ Retuns username (utf-8) """
    	return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})


class Driver(User):
    """ Driver model """

    photo = models.URLField(blank=True)
    # Instead of description and interests we should just have a bio
    description = models.CharField(blank=True, max_length=1000)
    interests = models.CharField(blank=True, max_length=500)
    # As well as a field to showcase all of the trips driven
    trips = ForeignKey(Trip)
    bike = models.CharField(blank=True, max_length=100)


class Rider(User):
    """ Rider model """

    # Might be useless but I'll leave it here in case I think of
    # something useful for it
    pass
