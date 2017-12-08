#!/usr/bin/env python
# -*- coding:utf-8 -*-
# arthur:Dear
# 2017-12-07 11:12:49

from django import forms
from django.utils.translation import gettext_lazy as _

from models import IDC, Asset, Server


class AssetCreateForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = [
            'type', 'hostname', 'status', 'intranet', 'internet', 'idc',
            'cabinet_num', 'cabinet_order', 'vendor', 'model', 'sn', 'comment'
        ]
        '''
        widgets = {
            'groups': forms.SelectMultiple(
                attrs={'class': 'select2',
                       'data-placeholder': _('Select asset groups')}),
            'admin_user': forms.Select(
                attrs={'class': 'select2',
                       'data-placeholder': _('Select asset admin user')}),
        }
        help_texts = {
            'intranet': '* required',
        }
        '''


class ServerCreateForm(forms.ModelForm):
    class Meta:
        model = Server
        fields = [
            'hostname', 'host', 'status', 'intranet', 'internet', 'env','comment'
        ]


class IDCCreateForm(forms.ModelForm):
    class Meta:
        model = IDC
        fields = [
            'name', 'contact', 'phone', 'address', 'comment'
        ]
