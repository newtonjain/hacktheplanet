# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20150815_2258'),
        ('users', '0006_auto_20150815_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='trip',
            field=models.ForeignKey(related_name='users', default=None, blank=True, to='api.Trip'),
            preserve_default=False,
        ),
    ]
