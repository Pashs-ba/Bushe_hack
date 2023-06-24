from django.apps import AppConfig


class BlogConfig(AppConfig):
    """Blog app config."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "backend.apps.blog"
    verbose_name = "Блог"
