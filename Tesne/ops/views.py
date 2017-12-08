# -*- coding: utf-8 -*-
from django.shortcuts import redirect, HttpResponse, render
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, View, DetailView

from utils.salt import LocalClient, WebAPI


client = LocalClient()
webapi = WebAPI()


def list_all_keys(request):
    keys = webapi.list_all_key()
    return HttpResponse(keys)


def cmd(request, tgt, func, *args, **kwargs):
    result = client.cmd(tgt, func, *args, **kwargs)
    return result

def cmd_async(request, tgt, func, *args, **kwargs):
    result = client.cmd_async(tgt, func, *args, **kwargs)
    return result
