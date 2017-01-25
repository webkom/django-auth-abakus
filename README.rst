django-auth-abakus |Build status|
=================================

A django auth module that can be used to to authenticate users against
the API of abakus.no. You need valid credentials for a Oauth2 application to use this library.
Contact webkom@abakus.no for more information.

Important Notice
----------------
Versions from 2.0 and higher is used to authenticate against the new abakus.no "LEGO".
Older versions support the old system called "NERD". As of 10.06.2016, "NERD" is
running in production.

Contribute
----------

Open an issue or a pull-request with your fix or awesome new feature.
Make sure to check those that are already open, to avoid duplicates.

Create release
--------------

Run `semantic-release publish` and the correct version number will be chosen and
commited/tagged before it is pushed to git and uploaded to pypi.

--------------

MIT © Webkom, Abakus Linjeforening

.. _documentation: http://django-auth-abakus.readthedocs.org/

.. |Build status| image:: https://ci.abakus.no/api/badges/webkom/django-auth-abakus/status.svg
   :target: https://ci.abakus.no/webkom/django-auth-abakus
