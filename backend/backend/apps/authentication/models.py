from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone


from .manager import UserManager
from .utils import ACCOUNT_TYPE_CHOICES, UserTypes

from backend.apps.core.utils import OrderStatus, ORDER_TYPE_CHOICES, DeliveryManStatus, DELIVERYMAN_TYPE_CHOICES


class User(AbstractBaseUser, PermissionsMixin):
    """User model."""

    account_type = models.IntegerField(
        "Тип аккаунта", default=UserTypes.COURIER, choices=ACCOUNT_TYPE_CHOICES
    )
    is_active = models.BooleanField("Активный", default=True)
    is_staff = models.BooleanField("Администратор", default=False)

    first_name = models.CharField("Имя", max_length=100)
    last_name = models.CharField("Фамилия", max_length=100)
    photo_url = models.URLField("Аватар", default=None, null=True)
    username = models.CharField("Логин", max_length=100, unique=True)
    telegram_id = models.IntegerField("Telegram ID")

    date_joined = models.DateTimeField("Дата регистрации", default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["account_type", "first_name", "telegram_id"]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    @property
    def is_admin(self) -> bool:
        """Check if user's an admin."""
        return self.account_type in [UserTypes.ROOT, UserTypes.MANAGER]

    def __str__(self):
        return self.get_username()


class Manager(models.Model):
    user = models.OneToOneField("User", on_delete=models.CASCADE)
    kitchen_id = models.ForeignKey("core.Kitchen", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class DeliveryMan(models.Model):
    user = models.OneToOneField("User", on_delete=models.CASCADE)
    status = models.IntegerField(choices=DELIVERYMAN_TYPE_CHOICES, default=DeliveryManStatus.ready.value)

    def __str__(self):
        return str(self.user)