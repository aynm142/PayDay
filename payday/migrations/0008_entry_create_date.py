# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-06 13:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payday', '0007_remove_entry_create_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='create_date',
            field=models.TimeField(default=datetime.datetime(2017, 7, 6, 16, 6, 4, 974537)),
        ),
    ]