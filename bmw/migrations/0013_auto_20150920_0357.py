# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bmw', '0012_trip_scenic_locations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='scenic_locations',
            field=models.ManyToManyField(to='address.Address'),
        ),
    ]
