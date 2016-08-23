from abakus.auth import AbakusBackend
from django.test import TestCase


class AbakusBackendTestCase(TestCase):

    def test_authorize(self):
        backend = AbakusBackend()
        backend.authenticate('webkom', 'webkom')
