from django.apps import AppConfig


class LifeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'life'

    def ready(self) -> None:
        import life.signals.handlers
