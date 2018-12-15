from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.course_list, name='course_list'),
    url(r'^create/$', views.course_create, name='course_create'),
    url(r'^courses/(?P<pk>\d+)/update/$', views.course_update, name='course_update'),
    url(r'^courses/(?P<pk>\d+)/delete/$', views.course_delete, name='course_delete'),
]
