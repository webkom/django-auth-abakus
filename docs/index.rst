django-auth-abakus |frigg| |coverage| |version| |python|
========================================================

A django auth module that can be used to to authenticate users against the API of abakus.no. If you
would like to use it you need a API token.

Contact webkom@abakus.no to request one.


Usage
=====

Set the authentication backend to *AbakusBackend: ::

    AUTHENTICATION_BACKENDS = ( 'abakus.auth.AbakusBackend', )


The token should be added in the django-settings as `ABAKUS_TOKEN`: ::

    ABAKUS_TOKEN = 'private_token'


Contribute
==========
Open an issue or a pull-request with your fix or awesome new feature.
Make sure to check those that are already open, to avoid duplicates.

Contents:

.. toctree::
   :maxdepth: 2

    Settings <settings>


.. |frigg| image:: https://ci.frigg.io/badges/webkom/django-auth-abakus/
    :target: https://ci.frigg.io/webkom/django-auth-abakus/last/
    :alt: Build

.. |coverage| image:: https://ci.frigg.io/badges/coverage/webkom/django-auth-abakus/
    :target: https://ci.frigg.io/webkom/django-auth-abakus/last/
    :alt: Coverage

.. |version| image:: https://pypip.in/version/django-auth-abakus/badge.svg?style=flat
    :target: https://pypi.python.org/pypi/django-auth-abakus/
    :alt: Latest Version

.. |python| image:: https://pypip.in/py_versions/django-auth-abakus/badge.svg?style=flat
    :target: https://pypi.python.org/pypi/django-auth-abakus/
    :alt: Supported Python versions
