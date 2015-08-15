# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models

from api.models import Trip
# from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    photo = models.URLField(blank=True)
    phone_number = models.IntegerField(blank=True, null=True)
    is_customer = models.BooleanField(max_length=100, default=True)
    description = models.CharField(blank=True, max_length=200)
    interests = models.CharField(blank=True, max_length=300)

    # relationships
    trip = models.ForeignKey(Trip, blank=True, null=True, related_name='users')

    def __unicode__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

    def send_text(self, status):
        '''Send a text message to this users phone.'''
        pass
