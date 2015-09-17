# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20150917_0400'),
        ('api', '0012_auto_20150816_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='end',
        ),
        migrations.RemoveField(
            model_name='route',
            name='start',
        ),
        migrations.RemoveField(
            model_name='route',
            name='trip',
        ),
        migrations.DeleteModel(
            name='Route',
        ),
        migrations.DeleteModel(
            name='Trip',
        ),
    ]
