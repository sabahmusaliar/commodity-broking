# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-17 06:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commodity', '0002_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_details', models.CharField(max_length=23)),
                ('quantity', models.IntegerField()),
                ('Date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_details', models.CharField(max_length=23)),
                ('quantity', models.IntegerField()),
                ('Date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]