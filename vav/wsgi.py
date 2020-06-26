"""
WSGI config for vav project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import json

from django.core.wsgi import get_wsgi_application
import firebase_admin
from firebase_admin import credentials

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vav.settings")
cred = credentials.Certificate("D:\disk_D\VISA 2020\Visa Google Cloud\VAV-BE\credentials.json")

default_app = firebase_admin.initialize_app(cred)
application = get_wsgi_application()