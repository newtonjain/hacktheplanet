# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_user_profile_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='profile_url',
            new_name='profile_picture_url',
        ),
    ]
