# -*- coding: utf-8 -*-
import requests
from django.conf import settings
from django.contrib.auth.models import Group

from .utils import get_user_model

path = ''.join([
    getattr(settings, 'ABAKUS_URL', 'https://abakus.no'),
    '/api/',
    settings.ABAKUS_TOKEN,
    '/user/check/'
])


class ApiError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class AbakusBackend(object):
    def authenticate(self, username, password):
        """
        Should try to login with abakus.no (NERD).
        """
        response = requests.post(url=path, data={'username': username, 'password': password})
        info = response.json()

        try:
            user_info = info['user']
        except KeyError:
            raise ApiError(info['status_message'])

        name = ''
        if 'name' in user_info:
            name = user_info['name']

        if not bool(user_info['auth']):
            return None

        if getattr(settings, 'ABAKUS_AUTH_REQUIRE_ABAKOM', False) and not user_info['is_abakom']:
            return None

        if hasattr(settings, 'ABAKUS_GROUP_REQUIRED'):
            if not self.has_required_group(user_info):
                return None

        user = get_user_model().objects.get_or_create(username=username)[0]
        user.is_active = True
        self.parse_name(user, name)
        user.save()

        if 'committees' in user_info:
            for committee in user_info['committees']:
                groups = Group.objects.filter(name=committee)
                if len(groups) == 1:
                    user.groups.add(groups[0])

        return user

    def get_user(self, user_id):
        try:
            return get_user_model().objects.get(pk=user_id)
        except get_user_model().DoesNotExist:
            return None

    @staticmethod
    def parse_name(user, name):
        names = name.split(' ')
        user.first_name = ' '.join(names[:len(names) - 1])
        user.last_name = names[len(names) - 1]

    @staticmethod
    def has_required_group(info):
        if 'committees' not in info:
            return False

        return bool([g for g in info['committees'] if g in settings.ABAKUS_GROUP_REQUIRED])
