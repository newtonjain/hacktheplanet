# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.contrib.auth.models
from django.conf import settings
import address.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '__first__'),
        ('address', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, primary_key=True, parent_link=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('users.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, primary_key=True, parent_link=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('bike_model', models.CharField(default='BMW G 650 GS', max_length=100, choices=[('BMW G 650 GS', 'BMW G 650 GS'), ('BMW F 700 GS', 'BMW F 700 GS'), ('BMW F 800 GS', 'BMW F 800 GS'), ('BMW S 1000 XR', 'BMW S 1000 XR')])),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('users.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('deleted_ts', models.DateTimeField(verbose_name='Deleted timestamp', null=True, editable=False, blank=True)),
                ('name', models.CharField(null=True, max_length=100, blank=True)),
                ('scenic', models.BooleanField(default=False)),
                ('start_ts', models.DateTimeField(default=django.utils.timezone.now, null=True, blank=True)),
                ('customer', models.ForeignKey(to='bmw.Customer', related_name='customer_trips')),
                ('driver', models.ForeignKey(to='bmw.Driver', related_name='driver_trips')),
                ('end', address.models.AddressField(null=True, to='address.Address', blank=True, related_name='ending_trips')),
                ('start', address.models.AddressField(null=True, to='address.Address', blank=True, related_name='starting_trips')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TripStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('deleted_ts', models.DateTimeField(verbose_name='Deleted timestamp', null=True, editable=False, blank=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
            ],
            options={
                'db_table': 'trip_statuses',
            },
        ),
        migrations.AddField(
            model_name='trip',
            name='status',
            field=models.ForeignKey(to='bmw.TripStatus'),
        ),
    ]
