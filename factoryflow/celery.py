from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Указываем Django настройки для Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'factoryflow.settings')

app = Celery('factoryflow')

# Используем строку настроек Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически обнаруживает все задачи в приложениях Django
app.autodiscover_tasks()