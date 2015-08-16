# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20150815_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='trip',
            field=models.ForeignKey(related_name='locations', blank=True, to='api.Trip'),
        ),
    ]
