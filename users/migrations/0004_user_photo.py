# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20150815_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.URLField(blank=True),
        ),
    ]
