# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-18 18:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commodity', '0003_buy_sell'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='Date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='adress',
            field=models.CharField(max_length=500),
        ),
    ]
