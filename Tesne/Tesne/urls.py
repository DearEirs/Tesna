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
from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^assets/', include('assets.urls')),
    url(r'^ops/', include('ops.urls')),
    url(r'^account/', include('account.urls')),
]

'''
url(r'^idc/add', idc_create),
url(r'^idc/delete/(?P<id>[0-9]+)', idc_delete),
url(r'^idc/update/(?P<id>[0-9]+)', idc_update),
url(r'^idc/list', idc_list),
url(r'^assets/add', add_assets, name='add_assets'),
url(r'^assets/update/(?P<id>[0-9]+)', update_assets, name='update_assets'),
url(r'^assets/delete/(?P<id>[0-9]+)', delete_assets, name='delete_assets'),
url(r'^assets/list/$', list_assets, name='list_assets'),
url(r'^assets/list/(?P<type>[a-z]+)$', list_assets, name='list_assets'),
url(r'^assets/list/(?P<type>[a-z]+)/(?P<id>[0-9]+)', list_assets, name='list_assets'),
'''
