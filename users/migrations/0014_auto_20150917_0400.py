# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20150816_1407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='interests',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_customer',
        ),
        migrations.RemoveField(
            model_name='user',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='user',
            name='trips',
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='description',
            field=models.TextField(max_length=1000, blank=True),
        ),
    ]
