# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-06 07:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0004_auto_20171206_0308'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AssetGroup',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='env',
        ),
    ]
