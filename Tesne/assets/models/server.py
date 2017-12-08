#!/usr/bin/env python
# -*- coding:utf-8 -*-
# arthur:Dear
# 2017-12-04 18:06:04


from django.db import models
from django.utils.translation import ugettext_lazy as _

from assets.models import Asset, ENV

class Server(models.Model):

    STATUS_CHOICES = (
        ('In use', _(u'开启')),
        ('Out of use', _(u'关闭')),
    )

    hostname = models.CharField(max_length=128, unique=True, verbose_name=_(u'主机名'), db_index=True)
    host = models.ForeignKey(Asset, blank=True, null=True, related_name=u'host', verbose_name=_(u'所属主机'))
    status = models.CharField(choices=STATUS_CHOICES, max_length=12, null=True, blank=True,
                              default='In use', verbose_name=_(u'状态'))
    env = models.ForeignKey(ENV, blank=True, null=True, related_name='env',
                            verbose_name=_(u'运行环境'),)
    intranet = models.GenericIPAddressField(max_length=32, verbose_name=_(u'内网IP'))
    internet = models.GenericIPAddressField(max_length=32, verbose_name=_(u'公网IP'))
    cpu_cores = models.IntegerField(null=True, verbose_name=_('CPU cores'))
    memory = models.CharField(max_length=64, null=True, blank=True, verbose_name=_('Memory'))
    disk = models.CharField(max_length=1024, null=True, blank=True, verbose_name=_('Disk info'))

    platform = models.CharField(max_length=128, null=True, blank=True, verbose_name=_('Platform'))
    os = models.CharField(max_length=128, null=True, blank=True, verbose_name=_('OS'))
    os_version = models.CharField(max_length=16, null=True, blank=True, verbose_name=_('OS version'))

    created_by = models.CharField(max_length=32, null=True, blank=True, verbose_name=_('Created by'))
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name=_('Date created'))
    date_updated = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Date updated'))
    comment = models.TextField(max_length=128, default='', blank=True, verbose_name=_(u'备注'))
