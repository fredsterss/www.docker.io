# settings/dotcloud.py
from settings.base import *

print "using dotcloud settings"

DEBUG = True
TEMPLATE_DEBUG = DEBUG

MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/dotcloud/data/media/'
STATIC_ROOT = '/home/dotcloud/volatile/static/'
STATIC_URL = '/static/'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', #
        'NAME': '/home/dotcloud/data/wwwdocker.db', # static location for db
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}