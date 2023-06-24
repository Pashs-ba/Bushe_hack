from django.apps import AppConfig


class HomeworkConfig(AppConfig):
    """Blog app config."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "backend.apps.homework"
    verbose_name = "Домашние задания"
