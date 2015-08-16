# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import address.models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('address', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', address.models.AddressField(blank=True, to='address.Address', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('scenic', models.BooleanField(default=False)),
                ('start_ts', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('customer', models.ForeignKey(related_name='customer_trips', to=settings.AUTH_USER_MODEL)),
                ('riders', models.ForeignKey(related_name='rider_trips', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='trip',
            field=models.ForeignKey(to='api.Trip'),
        ),
    ]
