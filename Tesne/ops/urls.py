"""D URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from ops.views import keys_list, key_accept, key_delete
from ops.views import JobCreateView, JobListView, JobDetailView

app_name = 'ops'

urlpatterns = [
    url(r'keys/list', keys_list, name='keys_list'),
    url(r'keys/(?P<key>[0-9a-zA-Z\.\_\-]+)/accept', key_accept, name='key_accept'),
    url(r'keys/(?P<key>[0-9a-zA-Z\.\_\-]+)/delete', key_delete, name='key_delete'),
    url(r'job/create', JobCreateView.as_view(), name='job_create'),
    url(r'job/list', JobListView.as_view(), name='job_list'),
    url(r'job/detail/(?P<job_id>\d+)', JobDetailView.as_view(), name='job_detail'),
]
