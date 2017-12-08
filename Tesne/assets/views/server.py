#!/usr/bin/env python
# -*- coding:utf-8 -*-
# arthur:Dear
# 2017-12-04 17:38:38

from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from django.views.generic import TemplateView, ListView, DetailView
from django.urls import reverse_lazy
from assets.models import Server
from django.utils import timezone
from assets import forms


class ServerCreateView(CreateView):
    model = Server
    form_class = forms.ServerCreateForm
    template_name = 'server/create_or_update.html'
    success_url = reverse_lazy('assets:server_list')

    def form_valid(self, form):
        self.server = server = form.save()
        server.created_by = self.request.user.username
        now = timezone.now()
        server.date_created = now
        server.date_updated = now
        server.save()
        print(server)
        return super(ServerCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = {
            'app': 'assets',
            'action': 'Create server',
        }
        kwargs.update(context)
        return super(ServerCreateView, self).get_context_data(**kwargs)


class ServerUpdateView(UpdateView):
    model = Server
    form_class = forms.ServerCreateForm
    template_name = 'server/create_or_update.html'
    success_url = reverse_lazy('assets:server_list')

    def form_valid(self, form):
        self.server = server = form.save()
        now = timezone.now()
        server.date_updated = now
        server.save()
        return super(ServerUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = {
            'app': 'assets',
            'action': 'Create server',
        }
        kwargs.update(context)
        return super(ServerUpdateView, self).get_context_data(**kwargs)


class ServerDeleteView(DeleteView):
    model = Server
    template_name = 'server/delete.html'
    success_url = reverse_lazy('assets:server_list')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


class ServerListView(ListView):
    model = Server
    template_name = 'server/list.html'
    success_url = reverse_lazy('assets:server_list')


class ServerDetailView(DetailView):
    model = Server
    template_name = 'server/detail.html'
    success_url = reverse_lazy('assets:server_list')
