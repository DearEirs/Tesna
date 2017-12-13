#!/usr/bin/env python
# -*- coding:utf-8 -*-
# arthur:Dear
# 2017-12-07 11:12:49

from django import forms
from django.utils.translation import gettext_lazy as _

from models import IDC, Asset, Server


class AssetCreateForm(forms.ModelForm):
    internet = forms.GenericIPAddressField(required=False, label=u'公网ip')

    class Meta:
        model = Asset
        fields = [
            'type', 'hostname', 'status', 'intranet', 'idc', 'internet',
            'cabinet_num', 'cabinet_order', 'vendor', 'model', 'sn', 'comment'
        ]


class ServerCreateForm(forms.ModelForm):
    internet = forms.GenericIPAddressField(required=False, label=u'公网ip')

    class Meta:
        model = Server
        fields = [
            'hostname', 'host', 'status', 'intranet', 'env','comment',
            'salt_id', 'internet'
        ]


class IDCCreateForm(forms.ModelForm):
    class Meta:
        model = IDC
        fields = [
            'name', 'contact', 'phone', 'address', 'comment'
        ]
