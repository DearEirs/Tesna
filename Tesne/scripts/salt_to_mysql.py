#!/usr/bin/env python
# -*- coding:utf-8 -*-
# arthur:Dear
# 2017-12-12 11:39:52

import os
import sys

import django
import salt.config
import salt.utils.event

project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] ='Tesne.settings'
django.setup()

from Tesne import settings
from ops.models import Job, Task


__opts__ = salt.config.client_config(settings.SALT_CONFIG)

events = salt.utils.event.MasterEvent(__opts__['sock_dir'])
for event in events.iter_events(full=True):
    if r'salt/job/' in event['tag']:
        data = event['data']
        job_id = data['jid']
        if data['fun'] != 'saltutil.find_job':
            if 'new' in event['tag']:
                targets = ','.join(data['minions'])
                job = Job.objects.filter(job_id=job_id)
                job.update(target=targets)
            elif 'ret' in event['tag']:
                print(event)
                job = Job.objects.get(job_id=job_id)
                task = Task.objects.create(job_id=job,
                                        salt_id=data['id'],
                                        date_finished=data['_stamp'],
                                        ret_code=data.get('retcode', '-1'),
                                        result=data['return'])
