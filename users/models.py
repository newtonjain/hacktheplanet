# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models

from api.models import Trip
# from django.utils.translation import ugettext_lazy as _


class Driver(User):

    def __init__(self):
    """ Initializes profile """
        photo = self.photo
    	phone_number = self.phone_number
    	description = self.description
    	interests = self.interests

    def __unicode__(self):
    	return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})


class Rider(User):

    def __init__(self):
    """ Initializes profile """
        photo = self.photo
    	phone_number = self.phone_number
    	description = self.description
    	interests = self.interests

    def __unicode__(self):
    	return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    photo = models.URLField(blank=True)
    phone_number = models.BigIntegerField(blank=True, null=True)
    is_customer = models.BooleanField(max_length=100, default=True)
    description = models.CharField(blank=True, max_length=1000)
    interests = models.CharField(blank=True, max_length=500)

    # relationships
    trips = models.ManyToManyField(Trip, blank=True, related_name='users')

    def __init__(self):
    	if is_customer:
	    return Rider(self)
	else:
	    return Driver(self)
