import os
from .base_settings import *

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "powerzoo",
        'USER': "user",
        'PASSWORD': "user123456",
        'HOST': 'database',
        'PORT': '5432',
    }
}

STATIC_ROOT = 'static'