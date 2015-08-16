# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='trip',
            field=models.ForeignKey(related_name='routes', blank=True, to='api.Trip'),
        ),
    ]
