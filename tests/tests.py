# -*- coding: utf-8 -*-
from django.test.utils import override_settings
from django.utils import unittest

import responses
from abakus.auth import AbakusBackend


class AuthenticationBackendTests(unittest.TestCase):
    def setUp(self):
        self.backend = AbakusBackend()

    def add_auth_api_response(self, body):
        responses.add(
            responses.POST,
            'https://abakus.no/api/token/user/check/',
            body=body,
            content_type='application/json'
        )

    @responses.activate
    def test_authenticate_success(self):
        self.add_auth_api_response('{"user": {"auth": true, "committees": "webkom", '
                                   '"name": "Albus Dumbledore"}}')
        user = self.backend.authenticate('test', 'test')
        self.assertIsNotNone(user)
        self.assertEqual(user.first_name, 'Albus')
        self.assertEqual(user.last_name, 'Dumbledore')

    @responses.activate
    def test_authenticate_failure(self):
        self.add_auth_api_response('{"user": {"auth": false}}')
        user = self.backend.authenticate('test', '')
        self.assertIsNone(user)

    @responses.activate
    @override_settings(ABAKUS_AUTH_REQUIRE_ABAKOM=True)
    def test_authenticate_is_abakom(self):
        self.add_auth_api_response('{"user": {"auth": true, "is_abakom": true, '
                                   '"name": "Albus Dumbledore"}}')

        user = self.backend.authenticate('test', 'test')
        self.assertIsNotNone(user)
        self.assertEqual(user.first_name, 'Albus')
        self.assertEqual(user.last_name, 'Dumbledore')

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
        self.assertIsNotNone(user)
        self.assertEqual(user.first_name, 'Albus')
        self.assertEqual(user.last_name, 'Dumbledore')

    @responses.activate
    @override_settings(ABAKUS_AUTH_REQUIRE_ABAKUS=True)
    def test_authenticate_is_not_abakus(self):
        self.add_auth_api_response('{"user": {"auth": true, "is_abakus": false}}')

        user = self.backend.authenticate('test', 'test')
        self.assertIsNone(user)

    @override_settings(ABAKUS_GROUP_REQUIRED=['webkom'])
    def test_group_required(self):
        self.assertFalse(self.backend.has_required_group({'committees': []}))
        self.assertFalse(self.backend.has_required_group({'committees': ['pr']}))
        self.assertTrue(self.backend.has_required_group({'committees': ['webkom']}))
        self.assertTrue(self.backend.has_required_group({'committees': ['pr', 'webkom', 'backup']}))


