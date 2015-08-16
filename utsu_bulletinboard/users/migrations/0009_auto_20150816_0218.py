# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20150816_0036'),
        ('users', '0008_auto_20150816_0036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='trips',
        ),
        migrations.AddField(
            model_name='user',
            name='trips',
            field=models.ManyToManyField(related_name='users', null=True, to='api.Trip', blank=True),
        ),
    ]
