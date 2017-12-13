#!/usr/bin/env python
# -*- coding:utf-8 -*-
# arthur:Dear
# 2017-12-07 11:12:49

from django import forms
from django.utils.translation import gettext_lazy as _

from models import Job


class JobCreateForm(forms.ModelForm):
    args = forms.CharField(required=False, label=u'参数')
    class Meta:
        model = Job
        fields = [
            'func', 'target', 'args'
        ]
