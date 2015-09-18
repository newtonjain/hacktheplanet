# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

SQL = '''
    INSERT INTO trip_statuses (name, description) VALUES
    ('REQUESTED', 'The trip has been requested and is waiting for approval.'),
    ('PICKING UP', 'Driver is on his way to pick up the customer.'),
    ('DRIVING', 'The Driver is now driving the customer.'),
    ('FINISHED', 'The Driver is done driving the customer.');
'''


class Migration(migrations.Migration):

    dependencies = [
        ('bmw', '0003_transaction'),
    ]

    operations = [
        migrations.RunSQL(SQL)
    ]
