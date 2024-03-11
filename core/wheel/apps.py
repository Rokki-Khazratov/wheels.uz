# wheel/apps.py
from django.apps import AppConfig

class WheelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wheel'

    def ready(self):
        import wheel.signals 