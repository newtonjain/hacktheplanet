# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20150815_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='customer',
            field=models.ForeignKey(related_name='customer_trips', blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='trip',
            name='rider',
            field=models.ForeignKey(related_name='rider_trips', blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
