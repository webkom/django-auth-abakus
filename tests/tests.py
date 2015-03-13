# -*- coding: utf-8 -*-
from django.contrib.auth.models import Group
from django.test import TestCase
from django.test.utils import override_settings

import responses
from abakus.auth import AbakusBackend, ApiError
from abakus.utils import get_user_model


class AuthenticationBackendBaseTestCase(TestCase):
    def setUp(self):
        self.backend = AbakusBackend()

    def tearDown(self):
        get_user_model().objects.all().delete()


class AuthenticationBackendTestCase(AuthenticationBackendBaseTestCase):
    def add_auth_api_response(self, body):
        responses.add(
            responses.POST,
            'https://abakus.no/api/token/user/check/',
            body=body,
            content_type='application/json'
        )

    def assertUser(self, user):
        self.assertIsNotNone(user)
        self.assertEqual(user.username, 'test')
        self.assertEqual(user.first_name, 'Albus')
        self.assertEqual(user.last_name, 'Dumbledore')

    @responses.activate
    def test_api_error(self):
        self.add_auth_api_response('{"status_message": "Bad token"}')
        self.assertRaises(ApiError, self.backend.authenticate, 'test', 'test')
        self.assertRaisesRegexp(ApiError, r'Bad token', self.backend.authenticate, 'test', 'test')

    @responses.activate
    def test_authenticate_success(self):
        self.add_auth_api_response('{"user": {"auth": true, "committees": ["webkom"], '
                                   '"name": "Albus Dumbledore"}}')
        user = self.backend.authenticate('test', 'test')
        self.assertUser(user)

    @responses.activate
    def test_authenticate_failure(self):
        self.add_auth_api_response('{"user": {"auth": false}}')
        user = self.backend.authenticate('test', '')
        self.assertIsNone(user)

    @responses.activate
    def test_groups(self):
        group = Group.objects.create(name='webkom')
        self.add_auth_api_response('{"user": {"auth": true, "committees": ["webkom"], '
                                   '"name": "Albus Dumbledore"}}')
        user = self.backend.authenticate('test', 'test')
        self.assertEqual(user.groups.all()[0].id, group.id)
        self.assertEqual(user.groups.all()[0].name, 'webkom')

        group.delete()

    @responses.activate
    @override_settings(ABAKUS_AUTH_REQUIRE_ABAKOM=True)
    def test_authenticate_is_abakom(self):
        self.add_auth_api_response('{"user": {"auth": true, "is_abakom": true, '
                                   '"name": "Albus Dumbledore"}}')

        user = self.backend.authenticate('test', 'test')
        self.assertUser(user)

    @responses.activate
    @override_settings(ABAKUS_GROUP_REQUIRED=['webkom'])
    def test_authenticate_is_abakom(self):
        self.add_auth_api_response('{"user": {"auth": true, "committees": ["webkom"], '
                                   '"name": "Albus Dumbledore"}}')

        user = self.backend.authenticate('test', 'test')
        self.assertUser(user)

    @responses.activate
    @override_settings(ABAKUS_GROUP_REQUIRED=['pr'])
    def test_authenticate_is_abakom(self):
        self.add_auth_api_response('{"user": {"auth": true, "committees": ["webkom"], '
                                   '"name": "Albus Dumbledore"}}')

        user = self.backend.authenticate('test', 'test')
        self.assertIsNone(user)

    @responses.activate
    @override_settings(ABAKUS_AUTH_REQUIRE_ABAKOM=True)
    def test_authenticate_is_not_abakom(self):
        self.add_auth_api_response('{"user": {"auth": true, "is_abakom": false}}')

        user = self.backend.authenticate('test', 'test')
        self.assertIsNone(user)

    @responses.activate
    @override_settings(ABAKUS_AUTH_REQUIRE_ABAKUS=True)
    def test_authenticate_is_abakus(self):
        self.add_auth_api_response('{"user": {"auth": true, "is_abakus": true,'
                                   ' "name": "Albus Dumbledore"}}')

        user = self.backend.authenticate('test', 'test')
        self.assertUser(user)

    @responses.activate
    @override_settings(ABAKUS_AUTH_REQUIRE_ABAKUS=True)
    def test_authenticate_is_not_abakus(self):
        self.add_auth_api_response('{"user": {"auth": true, "is_abakus": false}}')

        user = self.backend.authenticate('test', 'test')
        self.assertIsNone(user)

    @override_settings(ABAKUS_GROUP_REQUIRED=['webkom'])
    def test_group_required(self):
        self.assertFalse(self.backend.has_required_group({}))
        self.assertFalse(self.backend.has_required_group({'committees': []}))
        self.assertFalse(self.backend.has_required_group({'committees': ['pr']}))
        self.assertTrue(self.backend.has_required_group({'committees': ['webkom']}))
        self.assertTrue(self.backend.has_required_group({'committees': ['pr', 'webkom', 'backup']}))

    def test_get_user(self):
        get_user_model().objects.create(pk=1)
        self.assertEqual(self.backend.get_user(1).id, 1)
        self.assertEqual(self.backend.get_user(100), None)


@override_settings(ABAKUS_DUMMY_AUTH=True)
class DummyAuthenticationBackendTestCase(AuthenticationBackendBaseTestCase):

    def test_wrong_password(self):
        self.assertIsNone(self.backend.authenticate('u', 'wrong-password'))

    def test_superuser(self):
        user = self.backend.authenticate('superuser', 'abakus')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_staff(self):
        user = self.backend.authenticate('staff', 'abakus')
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_group(self):
        group = Group.objects.create(name='webkom')
        user = self.backend.authenticate('webkom', 'abakus')
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.groups.all()[0].name, 'webkom')
        group.delete()
