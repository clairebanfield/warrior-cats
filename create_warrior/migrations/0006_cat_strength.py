# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-03 21:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_warrior', '0005_auto_20160430_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='strength',
            field=models.IntegerField(default=25),
        ),
    ]
