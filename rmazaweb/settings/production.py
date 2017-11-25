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
ALLOWED_HOSTS = ['reparacionesmaza.com', 'localhost']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': os.environ['DB_HOST'],  # Set to empty string for localhost.
        'PORT': os.environ['DB_PORT'],  # Set to empty string for default.
        'CONN_MAX_AGE': 600,  # number of seconds database connections should persist for
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"
