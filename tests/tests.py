# -*- coding: utf-8 -*-
from django.test.utils import override_settings
from django.utils import unittest

import responses
from abakus.auth import AbakusBackend


class AuthenticationBackendTests(unittest.TestCase):
    def setUp(self):
        self.backend = AbakusBackend()

    @responses.activate
    def test_authenticate_success(self):
        responses.add(
            responses.POST,
            'https://abakus.no/api/token/user/check/',
            body='{"user": {"auth": true, "committees": "webkom", "name": "Albus Dumbledore"}}',
            content_type='application/json'
        )

        user = self.backend.authenticate('test', 'test')
        self.assertIsNotNone(user)
        self.assertEqual(user.first_name, 'Albus')
        self.assertEqual(user.last_name, 'Dumbledore')

    @responses.activate
    def test_authenticate_failure(self):
        responses.add(
            responses.POST,
            'https://abakus.no/api/token/user/check/',
            body='{"user": {"auth": false}}',
            content_type='application/json'
        )

        user = self.backend.authenticate('test', '')
        self.assertIsNone(user)

    @responses.activate
    @override_settings(ABAKUS_AUTH_REQUIRE_ABAKOM=True)
    def test_authenticate_success(self):
        responses.add(
            responses.POST,
            'https://abakus.no/api/token/user/check/',
            body='{"user": {"auth": true, "is_abakom": true, "name": "Albus Dumbledore"}}',
            content_type='application/json'
        )

        user = self.backend.authenticate('test', 'test')
        self.assertIsNotNone(user)
        self.assertEqual(user.first_name, 'Albus')
        self.assertEqual(user.last_name, 'Dumbledore')

    @responses.activate
    @override_settings(ABAKUS_AUTH_REQUIRE_ABAKOM=True)
    def test_authenticate_is_not_abakom(self):
        responses.add(
            responses.POST,
            'https://abakus.no/api/token/user/check/',
            body='{"user": {"auth": true, "is_abakom": false}}',
            content_type='application/json'
        )

        user = self.backend.authenticate('test', 'test')
        self.assertIsNone(user)
