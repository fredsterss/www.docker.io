# settings/dotcloud.py
#from wwwdocker.settings.base import *
#import json

print "using dotcloud settings"

DEBUG = False
TEMPLATE_DEBUG = DEBUG

MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/dotcloud/data/media/'
STATIC_ROOT = '/home/dotcloud/volatile/static/'
STATIC_URL = '/static/'
