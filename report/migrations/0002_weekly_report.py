# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-08 00:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='weekly_report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('sent', models.BooleanField(default=False)),
            ],
        ),
    ]
