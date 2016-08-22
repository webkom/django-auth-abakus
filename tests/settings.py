# -*- coding: utf8 -*-

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'abakus_auth',
        'HOST': '127.0.0.1'
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
