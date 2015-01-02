from django.conf.urls import patterns, url

from bigLoser import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<weight_id>\d+)/$', views.detail, name='detail'),
)