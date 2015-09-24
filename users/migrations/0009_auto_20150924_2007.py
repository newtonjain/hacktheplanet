# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20150922_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture_url',
            field=models.URLField(max_length=1000, null=True),
        ),
    ]
