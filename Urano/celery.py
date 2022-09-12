from __future__ import absolute_import

import os

from celery import Celery
from Urano.settings import base

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Urano.settings.development")

app = Celery("Urano")

app.config_from_object("Urano.settings.development", namespace="CELERY"),

app.autodiscover_tasks(lambda: base.INSTALLED_APPS)
