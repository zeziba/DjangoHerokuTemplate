"""
WSGI config for django_heroku_template project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

PROJECT_NAME = os.getenv("PROJECT_FOLDER")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'{ PROJECT_NAME }.settings')

application = get_wsgi_application()
