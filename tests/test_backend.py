import json

import responses
from django.test import TestCase

from abakus.auth import AbakusBackend

from . import fixtures


class AbakusBackendTestCase(TestCase):

    @responses.activate
    def test_authorize_superuser(self):
        responses.add(
            responses.POST,
            'http://api.abakus.no/authorization/token-auth/',
            body=json.dumps(fixtures.success_login),
            status=200,
            content_type='application/json'
        )

        backend = AbakusBackend()
        user = backend.authenticate('webkom', 'webkom')
        self.assertEquals(user.first_name, 'webkom')
        self.assertEquals(user.last_name, 'webkom')
        self.assertTrue(user.is_active, True)
        self.assertTrue(user.is_staff, True)
        self.assertTrue(user.is_superuser, True)
