# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='type_of_rider',
        ),
        migrations.AddField(
            model_name='user',
            name='is_customer',
            field=models.BooleanField(default=True, max_length=100),
        ),
    ]
