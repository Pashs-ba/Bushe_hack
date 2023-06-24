from backend.apps.authentication.models import User

from django.db import models


class Notification(models.Model):
    """Notification model.

    Messages that can be sent from admininstrators to other users.
    """

    CATEGORIES = (
        ("system", "System"),
        ("headteacher", "Headteacher"),
        ("event", "Event"),
    )

    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)
    title = models.CharField(max_length=255, default="")
    category = models.CharField(max_length=255, choices=CATEGORIES, default="system")

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Уведомление"
        verbose_name_plural = "Уведомления"
