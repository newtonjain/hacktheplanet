# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import address.models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '__first__'),
        ('bmw', '0009_auto_20150919_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='end',
            field=address.models.AddressField(to='address.Address', blank=True, related_name='ending_drivers', null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='start',
            field=address.models.AddressField(to='address.Address', blank=True, related_name='starting_drivers', null=True),
        ),
    ]
