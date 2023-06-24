from django.apps import AppConfig


class AuthConfig(AppConfig):
    """Authentication app config."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "backend.apps.authentication"
    verbose_name = "Авторизация"
