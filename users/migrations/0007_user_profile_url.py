# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_url',
            field=models.URLField(null=True),
        ),
    ]
