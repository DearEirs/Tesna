#!/usr/bin/env python
# -*- coding:utf-8 -*-
# arthur:Dear
# 2017-12-04 15:46:55

from django.db import models
from django.utils.translation import ugettext_lazy as _


class IDC(models.Model):
    ENV_CHOICES = (
        ('Server', _(u'服务器')),
        ('Switch', _(u'交换机')),
        ('Router', _(u'路由器')),
        ('Firewall', _(u'防火墙')),
    )
    name = models.CharField(max_length=32, verbose_name=_(u'名称'))
    contact = models.CharField(
        max_length=128, blank=True, verbose_name=_(u'联系人'))
    phone = models.CharField(max_length=32, blank=True,
                             verbose_name=_(u'联系电话'))
    address = models.CharField(
        max_length=128, blank=True, verbose_name=_(u"地址"))
    date_created = models.DateTimeField(
        auto_now_add=True, null=True, verbose_name=_('Date created'))
    created_by = models.CharField(
        max_length=32, blank=True, verbose_name=_('Created by'))
    comment = models.TextField(blank=True, verbose_name=_(u'备注'))

    def __unicode__(self):
        return self.name
