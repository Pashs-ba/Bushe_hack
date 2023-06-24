from django.apps import AppConfig


class CoreConfig(AppConfig):
    """Core app config."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "backend.apps.core"
    verbose_name = "Основное"
