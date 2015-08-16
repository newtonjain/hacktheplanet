# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20150816_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='description',
            field=models.CharField(max_length=500, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='interests',
            field=models.CharField(max_length=500, blank=True),
        ),
    ]
