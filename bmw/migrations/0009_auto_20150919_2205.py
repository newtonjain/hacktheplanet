# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bmw', '0008_auto_20150919_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='customer',
            field=models.ForeignKey(to='bmw.Customer', null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='driver',
            field=models.ForeignKey(to='bmw.Driver', null=True),
        ),
    ]
