from __future__ import annotations

from typing import Union

from backend.apps.core.models import Control, Group, Lesson, Quarter, Subject
from django.db import models
from django.utils.timezone import datetime


class HomeworkAttachment(models.Model):
    """Files that are attached to homework.

    Fields:
        file (`FileField`): File.
        homework (`ForeignKey`): Homework.
    """

    def homework_upload(instance: HomeworkAttachment, filename: str):
        """Return a path for a new homework attachment."""
        return "homework/{}_{}".format(instance.homework.id, filename)

    file = models.FileField("Файл", upload_to=homework_upload)
    homework = models.ForeignKey("Homework", on_delete=models.CASCADE, related_name="attachments")

    @property
    def size(self):
        return self.file.size

    class Meta:
        verbose_name = "Файл к заданию"
        verbose_name_plural = "Файлы к заданиям"


class Homework(models.Model):
    """Homework model."""

    lesson = models.ForeignKey(Lesson, verbose_name="Урок", on_delete=models.CASCADE)
    content = models.TextField("Задание", blank=True)

    class Meta:
        verbose_name = "Домашнее задание"
        verbose_name_plural = "Домашние задания"

    def __str__(self):
        return f"Домашнее задание от урока {self.lesson}"

    @property
    def files_attached(self) -> bool:
        """Check if there are files attached to the task."""
        return self.files.count > 0

    @property
    def subject(self) -> Subject:
        return self.lesson.group.subject

    @property
    def date(self) -> datetime.date:
        return self.lesson.date

    @property
    def group(self) -> Group:
        return self.lesson.group

    @classmethod
    def add_homework(
        cls,
        date: datetime.date,
        group: Group,
        content: Union[None, str] = None,
        files=None,
    ) -> Homework:
        """
        Add homework on the specified date and return it.

        Args:
            group: A group of students that do homework.
            date: A date on which the homework is added.
            content: Text with the task formatted with MarkDown.
            files: List of HomeworkFiles that are attached to the task.
        """
        if not content and not files:
            raise ValueError("Either content or files must be specified.")
        control = Control.get_default()
        if control is None:
            raise Exception("The default control is not defined.")
        quarter = Quarter.get_quarter_by_date(date)
        if quarter is None:
            raise Exception("Lesson's date can't be on holiday.")
        lesson = Lesson.objects.get_or_create(
            date=date, control=control, group=group, quarter=quarter
        )[0]
        homework = cls.objects.create(lesson=lesson, content=content)

        if files:
            HomeworkAttachment.objects.bulk_create(
                [HomeworkAttachment(file=f, homework=homework) for f in files]
            )
        return homework
