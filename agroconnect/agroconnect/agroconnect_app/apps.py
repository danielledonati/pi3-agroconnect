# Inside agroconnect_app/apps.py
from django.apps import AppConfig

class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'agroconnect_app'  # Ensure this matches your app name
