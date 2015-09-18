# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bmw', '0002_auto_20150918_0443'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('deleted_ts', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Deleted timestamp')),
                ('price', models.BigIntegerField()),
                ('driver', models.ForeignKey(to='bmw.Driver')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
