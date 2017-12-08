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
from assets.views import AssetCreateView, AssetUpdateView, AssetDeleteView, AssetListView, AssetDetailView
from assets.views import IDCCreateView, IDCUpdateView, IDCDeleteView, IDCListView
from assets.views import ServerCreateView, ServerUpdateView, ServerDeleteView, ServerListView, ServerDetailView


app_name = 'assets'


urlpatterns = [
    # idc
    url(r'idc/create', IDCCreateView.as_view(), name='idc_create'),
    url(r'idc/update/(?P<pk>[0-9]+)', IDCUpdateView.as_view(), name='idc_update'),
    url(r'idc/delete/(?P<pk>[0-9]+)', IDCDeleteView.as_view(), name='idc_delete'),
    url(r'idc/list/$', IDCListView.as_view(), name='idc_list'),
    # server
    url(r'server/create', ServerCreateView.as_view(), name='server_create'),
    url(r'server/update/(?P<pk>[0-9]+)', ServerUpdateView.as_view(), name='server_update'),
    url(r'server/delete/(?P<pk>[0-9]+)', ServerDeleteView.as_view(), name='server_delete'),
    url(r'server/list/$', ServerListView.as_view(), name='server_list'),
    url(r'server/detail/(?P<pk>[0-9]+)$', ServerDetailView.as_view(), name='server_detail'),
    # asset
    url(r'asset/create', AssetCreateView.as_view(), name='asset_create'),
    url(r'asset/update/(?P<pk>[0-9]+)', AssetUpdateView.as_view(), name='asset_update'),
    url(r'asset/delete/(?P<pk>[0-9]+)', AssetDeleteView.as_view(), name='asset_delete'),
    url(r'asset/list/$', AssetListView.as_view(), name='asset_list'),
    url(r'asset/detail/(?P<pk>[0-9]+)$', AssetDetailView.as_view(), name='asset_detail'),
    url(r'asset/list/(?P<type>[a-zA-Z]+)', AssetListView.as_view(), name='asset_list'),
    url(r'asset/list/(?P<pk>[0-9]+)', AssetListView.as_view(), name='asset_list')
]
