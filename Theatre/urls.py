from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'Theatre.views.home', name='home'),
    url(r'^merch/', 'Theatre.views.merch', name='merch'),
    url(r'^tickets/', 'Theatre.views.tickets', name='tickets'),
    url(r'^admin/', include(admin.site.urls)),
)
