from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7pepm9wkl7d=bpbrych*o$k$&qrnha+f6_l9uk#lkguv*y0_on'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
