from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import main.views

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='index'),
    url(r'^admin/', include(admin.site.urls)),
)
