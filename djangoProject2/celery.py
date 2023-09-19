import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject2.settings")
app = Celery("djangoProject2")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
