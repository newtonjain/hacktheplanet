# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20150816_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='trips',
            field=models.ManyToManyField(related_name='users', to='api.Trip', blank=True),
        ),
    ]
