#!/usr/bin/env python
import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

from django.test.utils import get_runner  # noqa
from django.conf import settings  # noqa
import django  # noqa

if django.VERSION >= (1, 7):
    django.setup()


def runtests():
    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=1, interactive=True)
    failures = test_runner.run_tests(['tests'])
    sys.exit(bool(failures))


if __name__ == '__main__':
    runtests()
