# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone

from api.models import Trip
# from django.utils.translation import ugettext_lazy as _


class Trip(models.Model):

    # real fields
	scenic = models.BooleanField(blank=True, default=False)
	start_ts = models.DateTimeField(blank=True, null=True, default=timezone.now)
	status = models.CharField(
		blank=True,
		default='unconfirmed',
		max_length=200)


class User(AbstractUser):

    def __init__(self, is_customer):
        """ Automatically defines user as driver or rider """
        if is_customer:
            return Rider(self)
        else:
            return Driver(self)


class Driver(User):

    photo = models.URLField(blank=True)
    phone_number = models.BigIntegerField(blank=True, null=True)
    description = models.CharField(blank=True, max_length=1000)
    interests = models.CharField(blank=True, max_length=500)
    trips = models.ForeignKey(Trips)

    def __unicode__(self):
        """ Retuns username (utf-8) """
    	return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})


class Rider(User):

    photo = models.URLField(blank=True)
    phone_number = models.BigIntegerField(blank=True, null=True)
    description = models.CharField(blank=True, max_length=1000)
    interests = models.CharField(blank=True, max_length=500)
    trips = models.ForeignKey(Trips)

    def __unicode__(self):
        """ Retuns username (utf-8) """
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
