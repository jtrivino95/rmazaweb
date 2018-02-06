from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7pepm9wkl7d=bpbrych*o$k$&qrnha+f6_l9uk#lkguv*y0_on'

# Default to dummy email backend. Configure dev/production/local backend
# as per https://docs.djangoproject.com/en/dev/topics/email/#email-backends
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
