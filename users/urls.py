from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
	path('', views.home, name='home'),
    url(r'^home$', views.homepage, name='index'),

    #path('users/', views.UserList, name='users'),
    
    url(r'^users/$', views.user_list, name='user_list'),
    url(r'^users/create/$', views.user_create, name='user_create'),
    url(r'^users/(?P<pk>\d+)/update/$', views.user_update, name='user_update'),
    url(r'^users/(?P<pk>\d+)/delete/$', views.user_delete, name='user_delete'),


    path('accounts/signup/student/', views.StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/teacher/', views.TeacherSignUpView.as_view(), name='teacher_signup'),

    #url(r'^userapi$', views.Get_users_List.as_view(), name='user_api'),
    #url(r'^userapi/(?P<pk>[0-9]+)$', views.UserDetail.as_view()),

]
