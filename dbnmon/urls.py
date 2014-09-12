from django.conf.urls import *
from dbnmon.views import dbnmon


urlpatterns = patterns('',
		url(r'^$',dbnmon),
		url(r'^index.html$',dbnmon),
		url(r'^resources/(?P<path>.*)$','django.views.static.serve',{'document_root':'/home/taylor/lesson/django/mysite/dbnmon/templates/resources'}),
		url(r'^html/(?P<path>.*)$','django.views.static.serve',{'document_root':'/home/taylor/lesson/django/mysite/dbnmon/templates/html'}),
		)
