from django.contrib import admin

from .models import Bell, TimetableLesson


class TimetableLessonAdmin(admin.ModelAdmin):
    """Configure the admin interface for the `TimetableLesson` model."""

    list_display = ("number", "day", "klass", "subject", "classroom")
    search_fields = ("number", "day", "klass", "subject", "classroom")


class BellAdmin(admin.ModelAdmin):
    """Configure the admin interface for the `Bell` model."""

    list_display = ("n",)


admin.site.register(TimetableLesson, TimetableLessonAdmin)
admin.site.register(Bell, BellAdmin)
