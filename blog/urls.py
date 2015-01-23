from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name = 'index'),
                       url(r'^about/$', views.about, name='about'),
                       url(r'^contact/$', views.contact, name='contact'),
                       url(r'^(?P<post_slug>[\w-]+)/$', views.view_post, name='view_post'))
