from django.conf.urls import patterns, url

from iots_app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^123/$', views.detail, name='detail'),
    url(r'^push/',views.PushView,name='PushView'),
    url(r'^PushList/',views.PushList,name='PushList'),
    url(r'^home/', views.home, name='home'),
    url(r'^query/', views.query, name='query'),
    url(r'^history/', views.history, name='history'),
    url(r'^online/', views.online, name='online'),

)
