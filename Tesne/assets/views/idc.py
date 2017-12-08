#!/usr/bin/env python
# -*- coding:utf-8 -*-
# arthur:Dear
# 2017-12-04 17:38:38

from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from django.views.generic import TemplateView, ListView, View
from django.urls import reverse_lazy
from assets.models import IDC
from django.utils import timezone
from assets import forms

class IDCCreateView(CreateView):
    model = IDC
    form_class = forms.IDCCreateForm
    template_name = 'idc/create_or_update.html'
    success_url = reverse_lazy('assets:idc_list')

    def form_valid(self, form):
        self.idc = idc = form.save()
        idc.created_by = self.request.user.username
        now = timezone.now()
        idc.date_created = now
        idc.date_updated = now
        idc.save()
        print(idc)
        return super(IDCCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = {
            'app': 'assets',
            'action': 'Create idc',
        }
        kwargs.update(context)
        return super(IDCCreateView, self).get_context_data(**kwargs)


class IDCUpdateView(UpdateView):
    model = IDC
    form_class = forms.IDCCreateForm
    template_name = 'idc/create_or_update.html'
    success_url = reverse_lazy('assets:idc_list')

    def form_valid(self, form):
        self.idc = idc = form.save()
        now = timezone.now()
        idc.date_updated = now
        idc.save()
        return super(IDCUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = {
            'app': 'assets',
            'action': 'Create idc',
        }
        kwargs.update(context)
        return super(IDCUpdateView, self).get_context_data(**kwargs)


class IDCDeleteView(DeleteView):
    model = IDC
    template_name = 'idc/delete.html'
    success_url = reverse_lazy('assets:idc_list')

    def get(self, *args, **kwargs):
        return self.post(args, kwargs)


class IDCListView(ListView):
    model = IDC
    template_name = 'idc/list.html'


class IDCDetailView(ListView):
    model = IDC
    template_name = 'idc/detail.html'

