# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20150815_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='trip',
            field=models.ForeignKey(to='api.Trip', blank=True),
        ),
    ]
