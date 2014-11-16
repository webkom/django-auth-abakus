# -*- coding: utf8 -*-

DEBUG = False
USE_SQLITE = False


ABAKUS_TOKEN = 'token'

try:
    from .local import USE_SQLITE
except ImportError:
    pass

if USE_SQLITE:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    }

else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'abakus_auth',
        }
    }


AUTH_USER_MODEL = 'tests.CustomUser'

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
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = 'supersecret'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'tests.urls'

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
