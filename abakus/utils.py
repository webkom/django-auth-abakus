# -*- coding: utf-8 -*-
import re

from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.functional import allow_lazy

first_cap_re = re.compile('(.)([A-Z][a-z]+)')
all_cap_re = re.compile('([a-z0-9])([A-Z])')

AUTH_USER_MODEL = settings.AUTH_USER_MODEL
get_user_model = allow_lazy(get_user_model, AUTH_USER_MODEL)


def camel_to_underscore(name):
    s1 = first_cap_re.sub(r'\1_\2', name)
    return all_cap_re.sub(r'\1_\2', s1).lower()


def underscoreize(data):
    if isinstance(data, dict):
        new_dict = {}
        for key, value in data.items():
            new_key = camel_to_underscore(key)
            new_dict[new_key] = underscoreize(value)
        return new_dict
    if isinstance(data, (list, tuple)):
        for i in range(len(data)):
            data[i] = underscoreize(data[i])
        return data
    return data
