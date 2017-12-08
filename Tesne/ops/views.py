# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from assets.models import Asset
from utils.salt import LocalClient, WebAPI


client = LocalClient()
webapi = WebAPI()

def list_all_keys(request):
    keys = webapi.list_all_key()
    return keys

def cmd(request, tgt, func, *args, **kwargs):
    result = client.cmd(tgt, func, *args, **kwargs)
    return result

def cmd_async(request, tgt, func, *args, **kwargs):
    result = client.cmd_async(tgt, func, *args, **kwargs)
    return result
