# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-12 07:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ops', '0003_auto_20171212_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_id',
            field=models.CharField(db_index=True, max_length=128, unique=True, verbose_name='Job_id'),
        ),
    ]
