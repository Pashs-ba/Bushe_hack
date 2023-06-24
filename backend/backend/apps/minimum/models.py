from backend.apps.core.models import Quarter
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Minimum(models.Model):
    """Educational minimum model."""

    GRADE_CHOICES = [(i, i) for i in range(4, 12)]
    SUBJECTS = [
        "Информатика",
        "История",
        "Литература",
        "Математика",
        "Обществознание",
        "Русский язык",
        "Хим-Био",
        "Экономика",
        "Физика",
    ]

    SUBJECT_CHOICES = [(i, i) for i in SUBJECTS]

    subject = models.CharField("Предмет", max_length=100, choices=SUBJECT_CHOICES)
    grade = models.IntegerField(
        "Класс", validators=[MaxValueValidator(11), MinValueValidator(4)], choices=GRADE_CHOICES
    )
    quarter = models.ForeignKey(Quarter, on_delete=models.PROTECT, verbose_name="Четверть")
    file = models.FileField("Файл")

    class Meta:
        ordering = ["grade", "subject", "quarter"]
        verbose_name_plural = "Минимумы"
        verbose_name = "Минимум"

    def __str__(self):
        return "{} - {} - {}".format(self.subject, self.grade, self.quarter)
