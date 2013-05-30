import os
import sys
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
os.environ['DJANGO_SETTINGS_MODULE'] = 'wwwdocker.settings.dotcloud'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
