from django.conf.urls import patterns, url

from bigLoser import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<weight_id>\d+)/$', views.detail, name='detail'),
    url(r'weight/add/$', views.WeightCreate.as_view(), name='weight_add'),
    url(r'weight/report/$', views.render_chart, name='render_chart'),
)