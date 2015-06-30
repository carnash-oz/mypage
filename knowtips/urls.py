from django.conf.urls import patterns, include, url

from knowtips.views import *

urlpatterns = patterns('',
    url(r'^bootstrap/?$', BootstrapView.as_view(), name='bootstrap'),
 	url(r'^django/?$', DjangoView.as_view(), name='django'),
    url(r'^android/?$', AndroidView.as_view(), name='android'),  

    url(r'^bootstrap/sidebar_example?$', SidebarExampleView.as_view(), name='sidebarexample'), 
    url(r'^bootstrap/adaptivewidth_example?$', AdaptiveWidthExampleView.as_view(), name='adaptivewidthexample'), 
    url(r'^bootstrap/bootstrapstuff_example?$', BootstrapStuffExampleView.as_view(), name='bootstrapstruffexample'), 
)