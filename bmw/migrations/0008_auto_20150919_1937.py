# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bmw', '0007_auto_20150919_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='trip_status',
            field=models.ForeignKey(blank=True, to='bmw.TripStatus', null=True),
        ),
    ]
