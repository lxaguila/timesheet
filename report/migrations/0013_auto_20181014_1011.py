# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-14 14:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0012_auto_20181014_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weekly_report',
            name='comments',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
