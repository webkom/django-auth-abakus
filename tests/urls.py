# -*- coding: utf8 -*-
from django.conf.urls import patterns, url, include

urlpatterns = patterns(
    '',
    url(r'^accounts/', include('django.contrib.auth.urls')),
)
