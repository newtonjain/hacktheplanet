# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150802_0428'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='interests',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='type_of_rider',
            field=models.CharField(default='Customer', max_length=100),
        ),
    ]
