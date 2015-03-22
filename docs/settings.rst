Settings
========

.. attribute:: ABAKUS_AUTH_REQUIRE_ABAKUS
    :noindex:

    **Default:** `False`

    Set `ABAKUS_AUTH_REQUIRE_ABAKUS = True` to require Abakus membership in order to authenticate.


.. attribute:: ABAKUS_AUTH_REQUIRE_ABAKOM
    :noindex:

    **Default:** `False`

    Set `ABAKUS_AUTH_REQUIRE_ABAKOM = True` to require committee membership in order to authenticate.


.. attribute:: ABAKUS_GROUP_REQUIRED
    :noindex:

    **Default:** `[]`

    ABAKUS_GROUP_REQUIRED is a list of required groups.

    Example: The user needs to be member of Webkom: ::

        ABAKUS_GROUP_REQUIRED = ['Webkom']


.. attribute:: ABAKUS_SUPERUSER_GROUPS
    :noindex:

    **Default:** `[]`

    ABAKUS_SUPERUSER_GROUPS is a list of committees with superuser access.

    Example: The user needs to be member of Webkom or HS: ::

        ABAKUS_SUPERUSER_GROUPS = ['Webkom', 'HS']
