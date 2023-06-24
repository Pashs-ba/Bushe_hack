from django.contrib import admin

from .models import Control, Group, Klass, Lesson, Quarter, Subject

admin.site.register(Subject)
admin.site.register(Lesson)
admin.site.register(Group)
admin.site.register(Control)
admin.site.register(Quarter)


class ClassAdmin(admin.ModelAdmin):
    """Admin configuration for `Klass` model."""

    list_display = ["name", "head_teacher", "description"]
    search_fields = ["name"]
    ordering = ["name"]


admin.site.register(Klass, ClassAdmin)
