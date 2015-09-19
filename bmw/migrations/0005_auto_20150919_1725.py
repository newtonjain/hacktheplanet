# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bmw', '0004_auto_20150918_1534'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trip',
            old_name='status',
            new_name='trip_status',
        ),
        migrations.AlterField(
            model_name='trip',
            name='customer',
            field=models.ForeignKey(related_name='customer_trips', to='bmw.Customer'),
        ),
    ]
