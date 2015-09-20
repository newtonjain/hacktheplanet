# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '__first__'),
        ('bmw', '0011_auto_20150919_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='scenic_locations',
            field=models.ManyToManyField(to='address.Address', null=True),
        ),
    ]
