# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '__first__'),
        ('api', '0008_location_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('end', models.ForeignKey(related_name='ending_addresses', blank=True, to='address.Address', null=True)),
                ('start', models.ForeignKey(related_name='starting_addresses', blank=True, to='address.Address', null=True)),
                ('trip', models.ForeignKey(related_name='locations', blank=True, to='api.Trip')),
            ],
        ),
        migrations.RemoveField(
            model_name='location',
            name='end',
        ),
        migrations.RemoveField(
            model_name='location',
            name='start',
        ),
        migrations.RemoveField(
            model_name='location',
            name='trip',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]
