from __future__ import absolute_import

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newapp.settings')

from django.conf import settings

app = Celery('newapp')

app.config_from_object(settings.CELERY)
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)