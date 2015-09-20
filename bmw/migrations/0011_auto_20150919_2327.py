# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import address.models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '__first__'),
        ('bmw', '0010_auto_20150919_2324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='end',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='start',
        ),
        migrations.AddField(
            model_name='driver',
            name='location',
            field=address.models.AddressField(blank=True, null=True, to='address.Address'),
        ),
    ]
