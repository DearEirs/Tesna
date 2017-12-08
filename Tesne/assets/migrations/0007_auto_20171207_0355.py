# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-07 03:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0006_auto_20171206_0848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='info',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='ip',
        ),
        migrations.RemoveField(
            model_name='server',
            name='info',
        ),
        migrations.AddField(
            model_name='asset',
            name='comment',
            field=models.TextField(blank=True, default=b'', max_length=128, verbose_name='Comment'),
        ),
        migrations.AddField(
            model_name='asset',
            name='cpu_cores',
            field=models.IntegerField(null=True, verbose_name='CPU cores'),
        ),
        migrations.AddField(
            model_name='asset',
            name='cpu_count',
            field=models.IntegerField(null=True, verbose_name='CPU count'),
        ),
        migrations.AddField(
            model_name='asset',
            name='cpu_model',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='CPU model'),
        ),
        migrations.AddField(
            model_name='asset',
            name='created_by',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='asset',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created'),
        ),
        migrations.AddField(
            model_name='asset',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Date updated'),
        ),
        migrations.AddField(
            model_name='asset',
            name='disk',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Disk info'),
        ),
        migrations.AddField(
            model_name='asset',
            name='internet',
            field=models.GenericIPAddressField(db_index=True, default=0, verbose_name='Outer IP'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='asset',
            name='intranet',
            field=models.GenericIPAddressField(db_index=True, default=0, verbose_name='Inner IP'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='asset',
            name='memory',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Memory'),
        ),
        migrations.AddField(
            model_name='asset',
            name='model',
            field=models.CharField(blank=True, max_length=54, null=True, verbose_name='Model'),
        ),
        migrations.AddField(
            model_name='asset',
            name='os',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='OS'),
        ),
        migrations.AddField(
            model_name='asset',
            name='os_version',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='OS version'),
        ),
        migrations.AddField(
            model_name='asset',
            name='platform',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Platform'),
        ),
        migrations.AddField(
            model_name='asset',
            name='sn',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Serial number'),
        ),
        migrations.AddField(
            model_name='asset',
            name='vendor',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Vendor'),
        ),
        migrations.AddField(
            model_name='server',
            name='comment',
            field=models.TextField(blank=True, default=b'', max_length=128, verbose_name='Comment'),
        ),
        migrations.AddField(
            model_name='server',
            name='cpu_cores',
            field=models.IntegerField(null=True, verbose_name='CPU cores'),
        ),
        migrations.AddField(
            model_name='server',
            name='created_by',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='server',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created'),
        ),
        migrations.AddField(
            model_name='server',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Date updated'),
        ),
        migrations.AddField(
            model_name='server',
            name='disk',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Disk info'),
        ),
        migrations.AddField(
            model_name='server',
            name='memory',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Memory'),
        ),
        migrations.AddField(
            model_name='server',
            name='os',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='OS'),
        ),
        migrations.AddField(
            model_name='server',
            name='os_version',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='OS version'),
        ),
        migrations.AddField(
            model_name='server',
            name='platform',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Platform'),
        ),
    ]
