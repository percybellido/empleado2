from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempleado1',
        'USER': 'neunapp1',
        'PASSWORD': 'neunappcursopro',
        'HOST': 'localhost',
        'PORT': '5432',

    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS= [BASE_DIR/'static']

MEDIA_URL='/media/'
MEDIA_ROOT= BASE_DIR/'media'