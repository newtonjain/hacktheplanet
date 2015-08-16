# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import address.models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '__first__'),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trip',
            old_name='riders',
            new_name='rider',
        ),
        migrations.RemoveField(
            model_name='location',
            name='location',
        ),
        migrations.AddField(
            model_name='location',
            name='end',
            field=address.models.AddressField(related_name='end_locations', blank=True, to='address.Address', null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='start',
            field=address.models.AddressField(related_name='start_locations', blank=True, to='address.Address', null=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='status',
            field=models.CharField(default=b'unconfirmed', max_length=200, blank=True),
        ),
    ]
