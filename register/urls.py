from django.conf.urls import patterns, url
from register import views

urlpatterns = patterns('',
	url(r'^$', views.register_user, name='register_user'),
	url(r'^success/$', views.register_success, name='register_success'),
)