from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	url(r'^bigLoser/', include('bigLoser.urls')),
	url(r'^register/', include('register.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
