from django.apps import AppConfig


class NotificationsConfig(AppConfig):
    """Config for the notifications app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "backend.apps.notifications"
    verbose_name = "Уведомления"
