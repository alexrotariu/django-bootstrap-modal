# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-12 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20180310_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='characters',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='book',
            name='summary',
            field=models.TextField(default=''),
        ),
    ]
