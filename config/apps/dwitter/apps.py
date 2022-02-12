from django.apps import AppConfig


class DwitterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'config.apps.dwitter'

    def ready(self):
        from . import signals
