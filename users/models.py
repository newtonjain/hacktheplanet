# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name = models.CharField(blank=True, max_length=100)
    description = models.TextField(blank=True, max_length=1000)
    facebook_id = models.BigIntegerField(null=True)
    phone_number = models.CharField(max_length=100, null=True)
    profile_picture_url = models.URLField(max_length=1000, null=True)
