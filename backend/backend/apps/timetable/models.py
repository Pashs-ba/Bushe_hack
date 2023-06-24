from __future__ import annotations

from datetime import date, datetime, time, timedelta

from backend.apps.core.models import Klass, Subject
from django.db import models


class Bell(models.Model):
    """Bell model.

    Represents lesson's number in a timetable.

    Fields:
        n (`IntegerField`): lesson number.
        start (`TimeField`): lesson start time.
        end (`TimeField`): lesson end time.
    """

    n = models.IntegerField(verbose_name="Номер урока")
    start = models.TimeField(verbose_name="Начало урока")
    end = models.TimeField(verbose_name="Конец урока")

    class Meta:
        ordering = ["n"]
        verbose_name = "Звонок"
        verbose_name_plural = "Звонки"

    def __str__(self):
        return "Урок №{}".format(self.n)

    @classmethod
    def generate_bell(cls, n: int) -> Bell:
        """Generate a new `Bell` object.

        This function should be used to generate a bell
        in case it's missing.
        """
        SCHOOL_DAY_START = datetime.combine(date.today(), time(9, 0, 0))
        BREAK = timedelta(minutes=15)
        LESSON_DURATION = timedelta(minutes=40)

        start = SCHOOL_DAY_START + n * LESSON_DURATION + n * BREAK
        end = start + LESSON_DURATION
        return cls.objects.create(n=n, start=start, end=end)

    @classmethod
    def get_or_generate(cls, n: int) -> Bell:
        try:
            bell = cls.objects.get(n=n)
        except cls.DoesNotExist:
            bell = cls.generate_bell(n)
        return bell


class TimetableLesson(models.Model):
    """TimetableLesson model.

    Represents a lesson in a timetable.

    Fields:
        number (`ForeignKey`): `Bell` model.
        day (`CharField`): Day of the week.
        klass (`ForeignKey`): `Klass` model.
        subject (`ForeignKey`): `Subject` model.
    """

    WEEKDAYS = (
        (1, "Monday"),
        (2, "Tuesday"),
        (3, "Wednesday"),
        (4, "Thursday"),
        (5, "Friday"),
        (6, "Saturday"),
        (7, "Sunday"),
    )

    klass = models.ForeignKey(
        Klass,
        models.CASCADE,
        related_name="lessons",
        verbose_name="Класс",
    )
    number = models.ForeignKey(Bell, models.CASCADE, verbose_name="Номер урока")
    subject = models.ForeignKey(Subject, models.CASCADE, verbose_name="Предмет")
    day = models.IntegerField("День недели", choices=WEEKDAYS)
    classroom = models.CharField("Кабинет", max_length=50, blank=True)

    class Meta:
        ordering = ["klass", "number"]
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        unique_together = ("number", "day", "klass", "subject")

    def __str__(self):
        return "{} - {} - {}".format(self.klass, self.number.n, self.subject)
