# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_user_trip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='trip',
            field=models.ForeignKey(null=True, to='api.Trip', blank=True, related_name='users'),
        ),
    ]
