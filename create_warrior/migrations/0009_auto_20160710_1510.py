# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-10 22:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('create_warrior', '0008_auto_20160710_1509'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cat',
            old_name='peception',
            new_name='perception',
        ),
    ]
