# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20150816_0036'),
        ('users', '0007_user_trip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='trip',
        ),
        migrations.AddField(
            model_name='user',
            name='trips',
            field=models.ForeignKey(null=True, blank=True, to='api.Trip', related_name='users'),
        ),
    ]
