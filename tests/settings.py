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

TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'

SECRET_KEY = 'supersecret'

ROOT_URLCONF = 'tests.urls'

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

ABAKUS_AUTH = {
    'SITE_URL': 'http://api.abakus.no',
}
