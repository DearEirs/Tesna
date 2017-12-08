#!coding:utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _

from assets.models import IDC


# Create your models here.


class Asset(models.Model):
    STATUS_CHOICES = (
        ('In use', _(u'开启')),
        ('Out of use', _(u'关闭')),
    )
    TYPE_CHOICES = (
        ('Server', _(u'服务器')),
        ('Switch', _(u'交换机')),
        ('Router', _(u'路由器')),
        ('Firewall', _(u'防火墙')),
    )

    type = models.CharField(choices=TYPE_CHOICES, max_length=16, blank=True, null=True,
                            default='Server', verbose_name=_(u'类别'),)
    hostname = models.CharField(max_length=128, unique=True, verbose_name=_(u'主机名'))
    intranet = models.GenericIPAddressField(max_length=32, verbose_name=_(u'内网IP'))
    internet = models.GenericIPAddressField(max_length=32, verbose_name=_(u'公网IP'))
    status = models.CharField(choices=STATUS_CHOICES, max_length=12, null=True, blank=True,
                              default='In use', verbose_name=_(u'状态'))
    idc = models.ForeignKey(IDC, blank=True, null=True, related_name='assets',
                            on_delete=models.SET_NULL, verbose_name=_('IDC'),)
    cabinet_num = models.CharField(max_length=128, verbose_name=_(u'机柜编号'))
    cabinet_order = models.CharField(max_length=128, verbose_name=_(u'机柜中的序号'))

    vendor = models.CharField(max_length=64, null=True, blank=True, verbose_name=_(u'供应商'))
    model = models.CharField(max_length=54, null=True, blank=True, verbose_name=_(u'型号'))
    sn = models.CharField(max_length=128, null=True, blank=True, verbose_name=_(u'SN码'))

    comment = models.TextField(max_length=128, default='', blank=True, verbose_name=_(u'备注'))

    cpu_model = models.CharField(max_length=64, null=True, blank=True, verbose_name=_(u'CPU型号'))
    cpu_count = models.IntegerField(null=True, verbose_name=_(u'CPU个数'))
    cpu_cores = models.IntegerField(null=True, verbose_name=_(u'CPU核心数'))
    memory = models.CharField(max_length=64, null=True, blank=True, verbose_name=_(u'内存'))
    disk = models.CharField(max_length=1024, null=True, blank=True, verbose_name=_(u'硬盘'))

    platform = models.CharField(max_length=128, null=True, blank=True, verbose_name=_(u'平台'))
    os = models.CharField(max_length=128, null=True, blank=True, verbose_name=_(u'系统'))
    os_version = models.CharField(max_length=16, null=True, blank=True, verbose_name=_(u'系统版本'))

    created_by = models.CharField(max_length=32, null=True, blank=True, verbose_name=_(u'创建人'))
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name=_(u'创建时间'))
    date_updated = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_(u'修改时间'))

    def __unicode__(self):
        return self.hostname
