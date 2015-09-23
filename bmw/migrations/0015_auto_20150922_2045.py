# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

SQL = '''
    INSERT INTO trip_statuses (name, description) VALUES
    ('ARRIVED', 'The driver has arrived at the customers location.');
'''


class Migration(migrations.Migration):

    dependencies = [
        ('bmw', '0014_auto_20150920_0404'),
    ]

    operations = [
        migrations.RunSQL(SQL)
    ]
