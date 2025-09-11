from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wtAPI.settings')

app = Celery('wtAPI')
app.config_from_object('django.conf:settings', namespace='CELERY')

# 使用 Redis 作为 Broker 和 Backend
app.conf.broker_url = 'redis://0.0.0.0:6379/0'
app.conf.result_backend = 'redis://0.0.0.0:6379/0'

app.autodiscover_tasks()


