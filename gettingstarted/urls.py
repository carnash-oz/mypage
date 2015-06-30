from django.conf.urls import patterns, include, url
from django.contrib import admin

from main.views import *

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='index'),
    url(r'^cv/$', CvView.as_view(), name='cv'),
    url(r'^gaming/$', GamingView.as_view(), name='gaming'),
    url(r'^admin/', include(admin.site.urls)),
)
