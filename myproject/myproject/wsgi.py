"""
WSGI config for myproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""
#import os
#import sys
#from django.core.wsgi import get_wsgi_application

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
#application = get_wsgi_application()
#application = get_wsgi_application()
#from whitenoise.django import DjangoWhiteNoise
#application = DjangoWhiteNoise(application)
#from dj_static import Cling
#application = Cling(get_wsgi_application())
#import os
#import sys
 
#path = '/home/<PythonAnywhere-username>/phocode-site'
#path = '/myproject/apps/myapp'
#if path not in sys.path:
# sys.path.append(path)
 
#os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'
 
#from django.core.wsgi import get_wsgi_application
#from django.contrib.staticfiles.handlers import StaticFilesHandler
#application = StaticFilesHandler(get_wsgi_application())
#-------
import os
import sys
"""
import signal
import traceback
import time
"""
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

#path = '/home/nidalmer/trailersapp/trailers/settings.py'
path = u'/home/pdtri/myproject'
if path not in sys.path:
    sys.path.append(path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
application = get_wsgi_application()
application = DjangoWhiteNoise(application)
