from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^blog/', include('blog.urls', namespace='blog')),
                        url(r'^', include('blog.urls', namespace='blog')),

    url(r'^admin/', include(admin.site.urls)),
)
