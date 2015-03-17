# -*- coding: utf-8 -*-
import django
from django.conf import settings
from django.utils.functional import allow_lazy


if django.VERSION >= (1, 5):
    from django.contrib.auth import get_user_model
    AUTH_USER_MODEL = settings.AUTH_USER_MODEL
    get_user_model = allow_lazy(get_user_model, AUTH_USER_MODEL)
else:
    from django.contrib.auth.models import User
    AUTH_USER_MODEL = 'auth.User'

    def get_user_model():
        return User
