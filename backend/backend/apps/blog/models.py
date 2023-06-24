from backend.apps.authentication.models import User
from django.db import models


class Posts(models.Model):
    """Posts model."""

    date = models.DateTimeField("Дата публикации", auto_now_add=True)
    title = models.CharField(max_length=100, verbose_name="Название")
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name="Автор",
        null=True,
        blank=True,
        related_name="posts",
    )
    content = models.TextField("Контент", blank=True)
    image = models.ImageField("Обложка", upload_to="blog/", blank=True, null=True)
    slug = models.SlugField("Ссылка", max_length=100, unique=True)

    class Meta:
        ordering = ["-date"]
        verbose_name_plural = "Записи"
        verbose_name = "Запись"

    def __str__(self):
        return "{}".format(self.title)
