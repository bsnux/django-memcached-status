django-memcached-status --  Arturo Fernandez <arturo@bsnux.com>
===============================================================

Description
-----------

Small Django application for displaying status information about *memcached* servers used in your *Django* applications.

Installation
------------

::

    $ python setup.py install

Configuring
-----------

Check that your **settings.py** has a line like this one:

::

    CACHE_BACKEND = 'memcached://127.0.0.1:11211?CACHE_BACKEND' 

Don't forget to include this application inside your **INSTALLED_APPS** section of your **settings.py** file:

::

    INSTALLED_APPS = (
        ...
        'django_memcached_status',
        ...
    )

Configuring your **urls.py**:

::

    urlpatterns = patterns('',
        (r'^memcached_status/',
          include("django_memcached_status.urls"))
    )

Don't forget to add **'django_memcached_status/templates/'** to your **TEMPLATE_DIRS** section inside your **settings.py** file

Usage
-------

::

    http://localhost:8000/memcached_status/server_list/
