import json

import responses
from django.test import TestCase

from abakus.auth import AbakusBackend
from abakus.settings import auth_settings

from . import fixtures


class AbakusBackendTestCase(TestCase):
    @responses.activate
    def test_authorize_superuser(self):
        responses.add(
            responses.POST,
            'http://api.abakus.no/authorization/token-auth/',
            body=json.dumps(fixtures.success_login_webkom),
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

    @responses.activate
    def test_bedkom(self):
        responses.add(
            responses.POST,
            'http://api.abakus.no/authorization/token-auth/',
            body=json.dumps(fixtures.success_login_bedkom),
            status=200,
            content_type='application/json'
        )

        backend = AbakusBackend()
        user = backend.authenticate('bedkom', 'bedkom')
        self.assertEquals(user.first_name, 'bedkom')
        self.assertEquals(user.last_name, 'bedkom')
        self.assertTrue(user.is_active, True)
        self.assertTrue(user.is_staff, False)
        self.assertTrue(user.is_superuser, False)

    @responses.activate
    def test_bad_auth(self):
        responses.add(
            responses.POST,
            'http://api.abakus.no/authorization/token-auth/',
            body=json.dumps(fixtures.invalid_login),
            status=400,
            content_type='application/json'
        )

        backend = AbakusBackend()
        user = backend.authenticate('user', 'invalid')
        self.assertEquals(user, None)


class RequireWebkomTestCase(TestCase):
    def setUp(self):
        self.OLD_REQUIRED_GROUPS = auth_settings.REQUIRED_GROUPS
        auth_settings.REQUIRED_GROUPS = ['Webkom']

    def tearDown(self):
        auth_settings.REQUIRED_GROUPS = self.OLD_REQUIRED_GROUPS

    @responses.activate
    def test_authorize_superuser(self, *args):
        responses.add(
            responses.POST,
            'http://api.abakus.no/authorization/token-auth/',
            body=json.dumps(fixtures.success_login_webkom),
            status=200,
            content_type='application/json'
        )

        backend = AbakusBackend()
        user = backend.authenticate('webkom', 'webkom')
        self.assertNotEqual(user, None)

    @responses.activate
    def test_normal_non_abakom_member(self, *args):
        responses.add(
            responses.POST,
            'http://api.abakus.no/authorization/token-auth/',
            body=json.dumps(fixtures.success_login_pleb),
            status=200,
            content_type='application/json'
        )

        backend = AbakusBackend()
        user = backend.authenticate('pleb', 'pleb')
        self.assertEquals(user, None)

    @responses.activate
    def test_bedkom(self):
        responses.add(
            responses.POST,
            'http://api.abakus.no/authorization/token-auth/',
            body=json.dumps(fixtures.success_login_bedkom),
            status=200,
            content_type='application/json'
        )

        backend = AbakusBackend()
        user = backend.authenticate('bedkom', 'bedkom')
        self.assertEquals(user, None)


class RequireAbakomTestCase(TestCase):
    def setUp(self):
        self.OLD_REQUIRE_ABAKOM = auth_settings.REQUIRE_ABAKOM
        auth_settings.REQUIRE_ABAKOM = True

    def tearDown(self):
        auth_settings.REQUIRE_ABAKOM = self.OLD_REQUIRE_ABAKOM

    @responses.activate
    def test_authorize_superuser(self, *args):
        responses.add(
            responses.POST,
            'http://api.abakus.no/authorization/token-auth/',
            body=json.dumps(fixtures.success_login_webkom),
            status=200,
            content_type='application/json'
        )

        backend = AbakusBackend()
        user = backend.authenticate('webkom', 'webkom')
        self.assertNotEqual(user, None)

    @responses.activate
    def test_normal_non_abakom_member(self, *args):
        responses.add(
            responses.POST,
            'http://api.abakus.no/authorization/token-auth/',
            body=json.dumps(fixtures.success_login_pleb),
            status=200,
            content_type='application/json'
        )

        backend = AbakusBackend()
        user = backend.authenticate('pleb', 'pleb')
        self.assertEqual(user, None)

    @responses.activate
    def test_bedkom_as_abakom_member(self):
        responses.add(
            responses.POST,
            'http://api.abakus.no/authorization/token-auth/',
            body=json.dumps(fixtures.success_login_bedkom),
            status=200,
            content_type='application/json'
        )

        backend = AbakusBackend()
        user = backend.authenticate('bedkom', 'bedkom')
        self.assertNotEqual(user, None)


class RequireBedkomTestCase(TestCase):
    def setUp(self):
        self.OLD_REQUIRED_GROUPS = auth_settings.REQUIRED_GROUPS
        auth_settings.REQUIRED_GROUPS = ['Bedkom']

    def tearDown(self):
        auth_settings.REQUIRED_GROUPS = self.OLD_REQUIRED_GROUPS

    @responses.activate
    def test_authorize_superuser(self, *args):
        responses.add(
            responses.POST,
            'http://api.abakus.no/authorization/token-auth/',
            body=json.dumps(fixtures.success_login_webkom),
            status=200,
            content_type='application/json'
        )

        backend = AbakusBackend()
        user = backend.authenticate('webkom', 'webkom')
        self.assertEquals(user, None)

    @responses.activate
    def test_normal_non_abakom_member(self, *args):
        responses.add(
            responses.POST,
            'http://api.abakus.no/authorization/token-auth/',
            body=json.dumps(fixtures.success_login_pleb),
            status=200,
            content_type='application/json'
        )

        backend = AbakusBackend()
        user = backend.authenticate('pleb', 'pleb')
        self.assertEquals(user, None)

    @responses.activate
    def test_bedkom(self):
        responses.add(
            responses.POST,
            'http://api.abakus.no/authorization/token-auth/',
            body=json.dumps(fixtures.success_login_bedkom),
            status=200,
            content_type='application/json'
        )

        backend = AbakusBackend()
        user = backend.authenticate('bedkom', 'bedkom')
        self.assertNotEqual(user, None)


class RequireAbakusMembership(TestCase):
    def setUp(self):
        self.OLD_REQUIRE_ABAKUS = auth_settings.REQUIRE_ABAKUS
        auth_settings.REQUIRE_ABAKUS = True

    def tearDown(self):
        auth_settings.REQUIRE_ABAKUS = self.OLD_REQUIRE_ABAKUS

    @responses.activate
    def test_pleb(self):
        responses.add(
            responses.POST,
            'http://api.abakus.no/authorization/token-auth/',
            body=json.dumps(fixtures.success_login_pleb),
            status=200,
            content_type='application/json'
        )

        backend = AbakusBackend()
        user = backend.authenticate('pleb', 'pleb')
        self.assertNotEqual(user, None)

    @responses.activate
    def test_alumni(self):
        responses.add(
            responses.POST,
            'http://api.abakus.no/authorization/token-auth/',
            body=json.dumps(fixtures.success_login_alumni_not_member),
            status=200,
            content_type='application/json'
        )

        backend = AbakusBackend()
        user = backend.authenticate('alumni', 'alumni')
        self.assertEquals(user, None)


class UserFieldsTestCase(TestCase):
    def setUp(self):
        self.OLD_POPULATE_USER_FIELDS = auth_settings.POPULATE_USER_FIELDS
        auth_settings.POPULATE_USER_FIELDS = []

    def tearDown(self):
        auth_settings.POPULATE_USER_FIELDS = self.OLD_POPULATE_USER_FIELDS

    @responses.activate
    def test_pleb(self):
        responses.add(
            responses.POST,
            'http://api.abakus.no/authorization/token-auth/',
            body=json.dumps(fixtures.success_login_pleb),
            status=200,
            content_type='application/json'
        )

        backend = AbakusBackend()
        user = backend.authenticate('pleb', 'pleb')
        self.assertNotEqual(user, None)
        with self.assertRaises(AttributeError):
            user.full_name
        with self.assertRaises(AttributeError):
            user.ical_token
        self.assertEqual(user.email, '')
