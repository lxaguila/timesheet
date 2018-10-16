# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-13 18:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0010_auto_20181013_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_log',
            name='end_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='daily_log',
            name='start_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
