from .base import *

import random
import string


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# DJANGO_SECRET_KEY *should* be specified in the environment. If it's not, generate an ephemeral key
if 'DJANGO_SECRET_KEY' in os.environ:
    SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
else:
    # Use if/else rather than a default value to avoid calculating this if we don't need it
    print("WARNING: DJANGO_SECRET_KEY not found in os.environ. Generating ephemeral SECRET_KEY.")
    SECRET_KEY = ''.join([random.SystemRandom().choice(string.printable) for i in range(50)])

# Hosts/domain names that are valid for this site; required if DEBUG is False
ALLOWED_HOSTS = ['reparacionesmaza.com']

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'rmazaweb',
        'USER': 'rmazaweb',
        'PASSWORD': 'rmazaweb',
        'HOST': '',  # Set to empty string for localhost.
        'PORT': '',  # Set to empty string for default.
        'CONN_MAX_AGE': 600,  # number of seconds database connections should persist for
    }
}