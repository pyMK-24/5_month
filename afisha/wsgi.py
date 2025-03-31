"""
WSGI config for afisha project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from read_env import read_env
from django.core.wsgi import get_wsgi_application
read_env(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'afisha.settings')

application = get_wsgi_application()
