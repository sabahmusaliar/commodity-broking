# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-23 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commodity', '0006_auto_20181020_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='sell',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='buy',
            name='product_details',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='buy',
            name='user',
            field=models.CharField(max_length=23),
        ),
        migrations.AlterField(
            model_name='sell',
            name='user',
            field=models.CharField(max_length=23),
        ),
    ]
