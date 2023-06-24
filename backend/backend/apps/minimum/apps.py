from django.apps import AppConfig


class MinimumConfig(AppConfig):
    """Minimum app config."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "backend.apps.minimum"
    verbose_name = "Образовательный минимум"
