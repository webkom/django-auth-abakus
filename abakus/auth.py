# -*- coding: utf-8 -*-
from django.contrib.auth.models import Group
from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session

from .settings import auth_settings
from .utils import get_user_model, underscoreize


class AbakusBackend(object):

    def authenticate(self, username, password):
        """
        Authenticate against the API.
        """
        username, password = username.strip(), password.strip()

        client_id = auth_settings.CLIENT_ID
        client_secret = auth_settings.CLIENT_SECRET

        client = LegacyApplicationClient(client_id=client_id)
        abakus = OAuth2Session(client=client)

        abakus.fetch_token(
            token_url=self.get_token_url(),
            username=username,
            password=password,
            client_id=client_id,
            client_secret=client_secret
        )

        response = abakus.get(self.get_user_url())

        if 300 > response.status_code >= 200:
            data = underscoreize(response.json())

            if not (auth_settings.REQUIRE_ABAKUS and data['is_abakus_member']):
                return None

            if not (auth_settings.REQUIRE_ABAKOM and data['is_abakom_member']):
                return None

            is_valid, is_superuser = self.validate_groups(data['groups'])

            if not is_valid:
                return None

            user_data = {key: data[key] for key in auth_settings.POPULATE_USER_FIELDS}
            user_data.update({'is_superuser': is_superuser, 'is_staff': is_superuser})

            user, _ = get_user_model().objects.update_or_create(
                username=data['username'],
                defaults=user_data
            )

            for group in data['groups']:
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
            [group for group in groups if group in required_groups]
        )
        is_superuser = not superuser_groups or bool(
            [group for group in groups if group in superuser_groups]
        )

        return is_valid, is_superuser

    def get_token_url(self):
        options = {
            'site_url': auth_settings.SITE_URL,
            'token_endpoint': auth_settings.TOKEN_ENDPOINT
        }
        return '{site_url}{token_endpoint}'.format(**options)

    def get_user_url(self):
        options = {
            'site_url': auth_settings.SITE_URL,
            'user_endpoint': auth_settings.USER_ENDPOINT
        }
        return '{site_url}{user_endpoint}'.format(**options)
