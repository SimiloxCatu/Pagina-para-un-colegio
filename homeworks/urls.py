from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.homework_list, name='homework_list'),
    url(r'^create/$', views.homework_create, name='homework_create'),
    url(r'^homeworks/(?P<pk>\d+)/update/$', views.homework_update, name='homework_update'),
    url(r'^homeworks/(?P<pk>\d+)/delete/$', views.homework_delete, name='homework_delete'),

]