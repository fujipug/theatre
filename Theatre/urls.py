from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'Theatre.views.home', name='home'),
    url(r'^merch/', 'Theatre.views.merch', name='merch'),
    url(r'^tickets/', 'Theatre.views.tickets', name='tickets'),
    url(r'^home_nontest_v/', 'Theatre.views.home_nontest_v', name='home_nontest_v'),
    url(r'^upcoming_performances/', 'Theatre.views.upcoming_performances', name='upcoming_performances'),
    url(r'^admin/', include(admin.site.urls)),
)
