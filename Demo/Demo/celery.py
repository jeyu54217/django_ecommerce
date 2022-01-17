import os
from celery import Celery

# Auto Switch between development & production
if not os.environ.get('DJANGO_SETTINGS_MODULE'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Demo.settings.dev')

# app instance == entry-point for everything you want to do in Celery ex. "app.config_from_object".
app = Celery('Demo',)

# Celery config / namespace:prefix of the celery config in setting ex. "CELERY_BROKER_URL".
app.config_from_object('django.conf:settings', namespace='CELERY') 

# autodiscove task from all registered Django apps.
app.autodiscover_tasks()

# Celery 5.1.2 documentation : https://docs.cyum 