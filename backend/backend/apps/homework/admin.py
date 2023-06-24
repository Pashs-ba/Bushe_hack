from django.contrib import admin

from .models import Homework, HomeworkAttachment

admin.site.register(Homework)
admin.site.register(HomeworkAttachment)
