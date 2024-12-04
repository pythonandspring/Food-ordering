from django.apps import AppConfig

class OrderingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ordering'

    def ready(self):
        import ordering.signals  # Ensure signals are loaded
