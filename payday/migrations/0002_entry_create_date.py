# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 11:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('payday', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='create_date',
            field=models.TimeField(default=datetime.datetime(2017, 6, 26, 11, 6, 56, 574506, tzinfo=utc)),
        ),
    ]
