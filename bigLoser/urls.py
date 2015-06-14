from django.conf.urls import patterns, url, include
from django.contrib import admin
from bigLoser import views

urlpatterns = patterns('',
    url(r'^(?P<user_id>\d+)/$', views.user_homepage, name ='user_homepage'),
    url(r'^admin_homepage/$', views.admin_homepage, name ='admin_homepage'),
    url(r'^contestant/(?P<contestant_id>\d+)/weight/add/$', views.WeightCreate.as_view(), name='weight_add'),
 	url(r'^contest/add/$', views.ContestCreate.as_view(), name='contest_add'),
 	url(r'^contestant/add/$', views.ContestantCreate.as_view(), name='contestant_add'),
 	url(r'^contestant/(?P<contestant_id>\d+)/$', views.contestant_homepage, name='contestant_homepage'),
 	url(r'^contestant/(?P<contestant_id>\d+)/report/$', views.render_chart, name='render_chart'),
)

urlpatterns += patterns('django.contrib.auth.views',
	url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
	url(r'^login/$', 'login',{'template_name': 'login.html'},name='bigLoser_login'),
	url(r'^logout/$', 'logout',{'next_page': 'index'},name='bigLoser_logout'),
)