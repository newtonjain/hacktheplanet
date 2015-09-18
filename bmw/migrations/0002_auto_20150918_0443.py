# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bmw', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='customer',
            field=models.ForeignKey(related_name='customer_trips', to='bmw.Customer', null=True),
        ),
    ]
