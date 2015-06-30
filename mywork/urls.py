from django.conf.urls import patterns, include, url

from mywork.views import *

urlpatterns = patterns('',
    url(r'^megaproyecto/?$', MegaproyectoView.as_view(), name='megaproyecto'),
)