# -*- coding: utf-8 -*-
from django.contrib.auth.models import Group

from abakus.utils import get_user_model

from .session import LegoSession
from .settings import auth_settings
from .utils import underscoreize


class AbakusBackend(object):

    def __init__(self):
        self.session = LegoSession()

    def authenticate(self, username, password):
        """
        Authenticate against the API.
        """
        username, password = username.strip(), password.strip()

        response = self.session.post(self.get_token_url(), json={
            'username': username,
            'password': password
        })

        if 300 > response.status_code >= 200:
            data = underscoreize(response.json()['user'])

            if auth_settings.REQUIRE_ABAKUS and not data['is_abakus_member']:
                return None

            if auth_settings.REQUIRE_ABAKOM and not data['is_abakom_member']:
                return None

            is_valid, is_superuser = self.validate_groups(data['abakus_groups'])

            if not is_valid:
                return None

            user_data = {key: data[key] for key in auth_settings.POPULATE_USER_FIELDS}
            user_data.update({'is_superuser': is_superuser, 'is_staff': is_superuser})

            user, _ = get_user_model().objects.update_or_create(
                username=data['username'],
                defaults=user_data
            )

            for group in data['abakus_groups']:
                try:
                    user_group = Group.objects.get(name=group)
                    user.groups.add(user_group)
                except Group.DoesNotExist:
                    pass

            return user

        return None

    def validate_groups(self, groups):
        """
        Check user groups against required groups.
        :return: a tuple (is_valid, is_superuser)
        """
        required_groups = auth_settings.REQUIRED_GROUPS
        superuser_groups = auth_settings.SUPERUSER_GROUPS

        is_valid = not required_groups or bool(
            [group['name'] for group in groups if group['name'] in required_groups]
        )
        is_superuser = not superuser_groups or bool(
            [group['name'] for group in groups if group['name'] in superuser_groups]
        )

        return is_valid, is_superuser

    def get_token_url(self):
        """
        Generate the token url used to login.
        """
        options = {
            'site_url': auth_settings.SITE_URL,
            'token_endpoint': auth_settings.TOKEN_ENDPOINT
        }
        return '{site_url}{token_endpoint}'.format(**options)
