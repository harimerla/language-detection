"""
WSGI config for Language_Detection project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os, sys
# add the hellodjango project path into the sys.path
path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(path, '/Language_Detection'))

# add the virtualenv site-packages path to the sys.path
sys.path.append('<PATH_TO_VIRTUALENV>/Lib/site-packages')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Language_Detection.settings')

application = get_wsgi_application()
