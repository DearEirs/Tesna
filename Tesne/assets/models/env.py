#!/usr/bin/env python
# -*- coding:utf-8 -*-
# arthur:Dear
# 2017-12-04 15:26:22

from django.db import models
from django.utils.translation import ugettext_lazy as _

class ENV(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name=_('Name'))

    def __unicode__(self):
        return self.name

