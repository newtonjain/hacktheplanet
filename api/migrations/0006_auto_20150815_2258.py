# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20150815_2240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='rider',
        ),
    ]
