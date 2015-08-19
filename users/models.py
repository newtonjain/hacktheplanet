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
    """ Trip model """

	scenic = models.BooleanField(blank=True, default=False)
	start_ts = models.DateTimeField(blank=True, null=True, default=timezone.now)
	status = models.CharField(blank=True, default='unconfirmed', max_length=200)

    # Why isn't this a thing?
    # def __unicode__(self):
    #     pass some shit


class User(models.Model):
    """ User model """

    name = models.CharField(blank=True, max_length=100)
    phone_number = models.BigIntegerField(blank=True, null=True)
    photo = models.URLField(blank=True)
    description = models.CharField(blank=True, max_length=1000)
    interests = models.CharField(blank=True, max_length=500)

    def __unicode__(self):
        """ Retuns username (utf-8) """
    	return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})



class Driver(models.Model):
    """ Driver model """

    user = models.ForeignKey(User)
    # Drivers definitely should have their own additional fields


class Rider(models.Model):
    """ Rider model """

    user = models.ForeignKey(User)
    # Might be useless but I'll leave it here in case I think of
    # something useful for it
