import httplib
import urllib
import json

from django.conf import settings
from django.contrib.auth.models import Group

from .utils import get_user_model

HEADERS = {
    "Content-type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
}

path = ''.join(['/api/', settings.ABAKUS_TOKEN, '/user/check/'])


class AbakusBackend:
    def authenticate(self, username, password):
        """
        Should try to login with abakus.no (NERD).
        """
        params = urllib.urlencode({'username': username, 'password': password})
        connection = httplib.HTTPSConnection(getattr(settings, 'ABAKUS_URL', 'abakus.no'))
        connection.request("POST", path, params, HEADERS)
        response = connection.getresponse()
        user_info = json.load(response)['user']

        name = ''
        if 'name' in user_info:
            name = user_info['name']

        if not bool(user_info['auth']) or len(user_info['committees']) == 0:
            return None

        user = get_user_model().objects.get_or_create(username=username)[0]
        user.is_active = True
        user.first_name = name
        user.save()

        if 'committees' in user_info:
            for committee in user_info['committees']:
                g = Group.objects.filter(name=committee)
                if len(g) == 1:
                    user.groups.add(g[0])

        return user

    def get_user(self, user_id):
        try:
            return get_user_model().objects.get(pk=user_id)
        except get_user_model().DoesNotExist:
            return None
