from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name = 'index'),
                       url(r'^/(?P<post_slug>[\w-]+)/$', views.view_post, name='view_post'))
