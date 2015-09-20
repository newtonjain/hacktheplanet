# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bmw', '0005_auto_20150919_1725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='start_ts',
        ),
        migrations.AlterField(
            model_name='trip',
            name='driver',
            field=models.ForeignKey(related_name='driver_trips', to='bmw.Driver', null=True),
        ),
    ]
