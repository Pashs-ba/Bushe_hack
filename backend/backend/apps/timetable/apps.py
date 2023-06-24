from django.apps import AppConfig


class TimetableConfig(AppConfig):
    """Config for the `timetable` app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "backend.apps.timetable"
    verbose_name = "Расписание"
