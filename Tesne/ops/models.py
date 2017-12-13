# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.



class Job(models.Model):
    job_id = models.CharField(max_length=128, verbose_name=_('Job_id'), db_index=True)
    func = models.CharField(max_length=128, null=False, verbose_name=_(u'方法'))
    target = models.CharField(max_length=128, null=False, verbose_name=_(u'目标机器'))
    args = models.CharField(max_length=128, verbose_name=_(u'参数'))
    date_start = models.DateTimeField(auto_now_add=True, verbose_name=_(u'开始时间'))
    created_by = models.CharField(max_length=128, null=False, verbose_name=_(u'创建人'))
    is_finish = models.BooleanField(default=False, verbose_name=_(u'是否完成'))
    is_success = models.BooleanField(default=False, verbose_name=_(u'是否成功'))

    def __unicode__(self):
        return self.job_id


class Task(models.Model):
    job_id = models.ForeignKey(Job, null=True)
    salt_id = models.CharField(max_length=128, verbose_name=_('Job_id'))
    date_finished = models.DateTimeField(blank=True, null=True, verbose_name=_(u'完成时间'))
    ret_code = models.IntegerField()
    result = models.TextField(blank=True, null=True, verbose_name=_(u'返回结果'))
