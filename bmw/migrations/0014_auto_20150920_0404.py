# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bmw', '0013_auto_20150920_0357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='customer',
            field=models.ForeignKey(null=True, related_name='customer_trips', to='bmw.Customer'),
        ),
    ]
