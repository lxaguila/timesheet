# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-11 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0006_auto_20181010_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_log',
            name='extra_time',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='daily_log',
            name='lunch_time',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='daily_log',
            name='travel_time',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
