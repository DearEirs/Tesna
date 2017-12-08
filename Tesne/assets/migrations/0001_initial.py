# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-05 10:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, choices=[(b'Server', 'Server'), (b'Switch', 'Switch'), (b'Router', 'Router'), (b'Firewall', 'Firewall')], default=b'Server', max_length=16, null=True, verbose_name='Asset type')),
                ('ip', models.GenericIPAddressField(db_index=True, verbose_name='IP')),
                ('hostname', models.CharField(max_length=128, unique=True, verbose_name='Hostname')),
                ('env', models.CharField(blank=True, choices=[(b'Prod', b'Production'), (b'Dev', b'Development'), (b'UAT', b'UAT')], default=b'Prod', max_length=8, null=True, verbose_name='Asset environment')),
                ('status', models.CharField(blank=True, choices=[(b'In use', 'In use'), (b'Out of use', 'Out of use')], default=b'In use', max_length=12, null=True, verbose_name='Asset status')),
            ],
        ),
        migrations.CreateModel(
            name='AssetGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Name')),
                ('created_by', models.CharField(blank=True, max_length=32, verbose_name='Created by')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created')),
                ('comment', models.TextField(blank=True, verbose_name='Comment')),
            ],
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Name')),
                ('contact', models.CharField(blank=True, max_length=128, verbose_name='Contact')),
                ('phone', models.CharField(blank=True, max_length=32, verbose_name='Phone')),
                ('address', models.CharField(blank=True, max_length=128, verbose_name='Address')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created')),
                ('created_by', models.CharField(blank=True, max_length=32, verbose_name='Created by')),
                ('comment', models.TextField(blank=True, verbose_name='Comment')),
                ('cabinet_number', models.IntegerField(verbose_name='cabinet_number')),
                ('cabinet_orde', models.IntegerField(verbose_name='cabinet_orde')),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor', models.CharField(blank=True, max_length=64, null=True, verbose_name='Vendor')),
                ('model', models.CharField(blank=True, max_length=54, null=True, verbose_name='Model')),
                ('sn', models.CharField(blank=True, max_length=128, null=True, verbose_name='Serial number')),
                ('cpu_model', models.CharField(blank=True, max_length=64, null=True, verbose_name='CPU model')),
                ('cpu_count', models.IntegerField(null=True, verbose_name='CPU count')),
                ('cpu_cores', models.IntegerField(null=True, verbose_name='CPU cores')),
                ('memory', models.CharField(blank=True, max_length=64, null=True, verbose_name='Memory')),
                ('disk_total', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Disk total')),
                ('disk_info', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Disk info')),
                ('platform', models.CharField(blank=True, max_length=128, null=True, verbose_name='Platform')),
                ('os', models.CharField(blank=True, max_length=128, null=True, verbose_name='OS')),
                ('os_version', models.CharField(blank=True, max_length=16, null=True, verbose_name='OS version')),
                ('os_arch', models.CharField(blank=True, max_length=16, null=True, verbose_name='OS arch')),
                ('hostname_raw', models.CharField(blank=True, max_length=128, null=True, verbose_name='Hostname raw')),
                ('created_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='Created by')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created')),
                ('comment', models.TextField(blank=True, default=b'', max_length=128, verbose_name='Comment')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='asset',
            name='idc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assets', to='assets.IDC', verbose_name='IDC'),
        ),
        migrations.AddField(
            model_name='asset',
            name='info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assets', to='assets.Info'),
        ),
    ]
