from django.shortcuts import redirect, HttpResponse, render
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, View, DetailView
from django.utils import timezone

from assets.models import Asset, IDC, ENV
from assets import forms


class AssetCreateView(CreateView):
    model = Asset
    form_class = forms.AssetCreateForm
    template_name = 'asset/create_or_update.html'
    success_url = reverse_lazy('assets:asset_list')

    def form_valid(self, form):
        self.asset = asset = form.save()
        asset.created_by = self.request.user.username
        now = timezone.now()
        asset.date_created = now
        asset.date_updated = now
        asset.save()
        return super(AssetCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = {
            'app': 'Assets',
            'action': 'Create asset',
        }
        kwargs.update(context)
        return super(AssetCreateView, self).get_context_data(**kwargs)


class AssetUpdateView(UpdateView):
    model = Asset
    form_class = forms.AssetCreateForm
    template_name = 'asset/create_or_update.html'
    success_url = reverse_lazy('assets:asset_list')

    def form_valid(self, form):
        self.asset = asset = form.save()
        now = timezone.now()
        asset.date_updated = now
        asset.save()
        return super(AssetUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = {
            'app': 'Assets',
            'action': 'Create asset',
        }
        kwargs.update(context)
        return super(AssetUpdateView, self).get_context_data(**kwargs)


class AssetDeleteView(DeleteView):
    model = Asset
    template_name = 'asset/delete.html'
    success_url = reverse_lazy('assets:asset_list')

    def get(self, *arg, **kwargs):
        return self.post(*arg, **kwargs)


class AssetListView(ListView):
    model = Asset
    template_name = 'asset/list.html'


class AssetDetailView(DetailView):
    model = Asset
    template_name = 'asset/detail.html'
