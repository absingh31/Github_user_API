# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_report_for_month_report_for_today_report_for_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='image_for_thumbnail',
            field=models.CharField(default='Well..', max_length=500),
        ),
    ]