# celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Define o settings padrão do Django para o Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

# Lê a configuração do Celery a partir das configurações do Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Descobre automaticamente tasks nos apps instalados
app.autodiscover_tasks()
