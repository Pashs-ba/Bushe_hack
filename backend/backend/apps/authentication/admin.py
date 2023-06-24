from django.contrib import admin

from .models import Student, Teacher, User


class UserAdmin(admin.ModelAdmin):
    """User admin configuration."""

    list_display = ("email", "first_name", "surname", "last_login")
    list_filter = ("account_type", "last_login")


admin.site.register(User, UserAdmin)
admin.site.register(Student)
admin.site.register(Teacher)
