# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-07 06:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0009_auto_20171207_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='sn',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='SN\u7801'),
        ),
    ]