# -*- coding: utf8 -*-
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


class Settings(object):

    DEFAULTS = {
        'TOKEN_ENDPOINT': '/authorization/token-auth/',

        'SITE_URL': 'https://abakus.no',
        'POPULATE_USER_FIELDS': ['email', 'first_name', 'last_name', 'is_active'],

        'REQUIRED_GROUPS': [],
        'SUPERUSER_GROUPS': [],

        'REQUIRE_ABAKUS': False,
        'REQUIRE_ABAKOM': False
    }

    def __getattr__(self, item):
        default_value = self.DEFAULTS.get(item)
        auth_settings = getattr(settings, 'ABAKUS_AUTH', {})
        settings_value = auth_settings.get(item)

        if settings_value is not None:
            return settings_value

        if default_value is not None:
            return default_value

        raise ImproperlyConfigured('Please set {option} in your ABAKUS_AUTH config.'.format(
            option=item
        ))


auth_settings = Settings()
