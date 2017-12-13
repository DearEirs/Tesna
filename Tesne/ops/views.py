# -*- coding: utf-8 -*-
from django.shortcuts import redirect, HttpResponse, render
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, View, DetailView

from ops import forms
from ops.models import Task, Job
from utils.salt import LocalClient, WebAPI
from django.utils import timezone

client = LocalClient()
webapi = WebAPI()


def keys_list(request):
    keys = webapi.list_all_key()
    return render(request, 'list_keys.html', keys)


def key_delete(request, key):
    result = webapi.delete_key(key)
    return redirect('/ops/keys/list.html')


def key_accept(request, key):
    result = webapi.accept_key(key)
    return redirect('/ops/keys/list.html')




def cmd_async(request, tgt, func, *args, **kwargs):
    result = client.cmd_async(tgt, func, *args, **kwargs)
    return result


class JobCreateView(CreateView):
    model = Job
    form_class = forms.JobCreateForm
    template_name = 'job_create.html'
    success_url = reverse_lazy('ops:job_list')

    def form_valid(self, form):
        self.job = job = form.save()
        job.created_by = self.request.user.username
        job.created_by = 'Dear'
        job.job_id = self.__cmd_exec(job.target, job.func, (job.args,))
        job.save()
        return super(JobCreateView, self).form_valid(form)

    def __cmd_exec(request, tgt, func, *args, **kwargs):
        result = client.cmd_async(tgt, func, *args, **kwargs)
        return result


class JobListView(ListView):
    model = Job
    template_name = 'job_list.html'

    def get_queryset(self):
        jobs = Job.objects.all().order_by('-date_start')
        return jobs



class JobDetailView(DetailView):
    model = Job
    slug_url_kwarg = 'job_id'
    template_name = 'job_detail.html'

    def get_object(self, queryset=None):
        job_id = self.kwargs.get(self.slug_url_kwarg, None)
        obj = Job.objects.get(job_id=job_id)
        return obj
