from django.conf.urls.defaults import *

urlpatterns = patterns('django_memcached_status.views',
                       (r'server_list/$', 'server_list'),
                      )
