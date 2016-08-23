# -*- coding: utf8 -*-

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    }
}

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',

    'abakus',
    'tests',
]
AUTHENTICATION_BACKENDS = 'abakus.auth.AbakusBackend',

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'

SECRET_KEY = 'supersecret'

ROOT_URLCONF = 'tests.urls'

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

ABAKUS_AUTH = {
    'SITE_URL': 'http://127.0.0.1:8000',
    'CLIENT_ID': 'test',
    'CLIENT_SECRET': 'test'
}
