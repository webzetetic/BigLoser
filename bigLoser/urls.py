from django.conf.urls import patterns, url, include
from django.contrib import admin
from bigLoser import views

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'weight/add/$', views.WeightCreate.as_view(), name='weight_add'),
    url(r'weight/report/$', views.render_chart, name='render_chart'),
    url(r'^(?P<user_id>\d+)/$', views.user_homepage, name = 'user_homepage')
)