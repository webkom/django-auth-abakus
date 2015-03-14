django-auth-abakus |Build status| |Coverage status|
===================================================

A django auth module that can be used to to authenticate users against
the API of abakus.no. If you would like to use it you need a API token.
Contact webkom@abakus.no to request one.

Usage
-----

Set the authentication backend to *AbakusBackend*

.. code:: python

        AUTHENTICATION_BACKENDS = ( 'abakus.auth.AbakusBackend', )

The token should be added in the django-settings as ``ABAKUS_TOKEN``.

For more information read the `documentation`_.

Contribute
----------

Open an issue or a pull-request with your fix or awesome new feature.
Make sure to check those that are already open, to avoid duplicates.

--------------

MIT © Webkom, Abakus Linjeforening

.. _documentation: http://django-auth-abakus.readthedocs.org/

.. |Build status| image:: https://ci.frigg.io/badges/webkom/django-auth-abakus/
   :target: https://ci.frigg.io/webkom/django-auth-abakus/last/
.. |Coverage status| image:: https://ci.frigg.io/badges/coverage/webkom/django-auth-abakus/
   :target: https://ci.frigg.io/webkom/django-auth-abakus/last/
