from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone


from .manager import UserManager
from .utils import ACCOUNT_TYPE_CHOICES, UserTypes


class User(AbstractBaseUser, PermissionsMixin):
    """User model."""
    account_type = models.IntegerField(
        "Тип аккаунта", default=UserTypes.DELIVER, choices=ACCOUNT_TYPE_CHOICES
    )
    is_active = models.BooleanField("Активный", default=True)
    is_staff = models.BooleanField("Администратор", default=False)
    name = models.CharField("Имя", max_length=100)
    surname = models.CharField("Фамилия", max_length=100)
    username = models.CharField("Логин", max_length=100, unique=True)
    telegram_id = models.BigIntegerField("Telegram ID")
    date_joined = models.DateTimeField("Дата регистрации", default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["account_type", "name", "surname", "telegram_id"]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
    @property
    def is_admin(self) -> bool:
        """Check if user's an admin."""
        return self.account_type in [UserTypes.ROOT, UserTypes.ADMIN]

    def __str__(self):
        return self.get_username()




class Admin(models.Model):
    """
    Options for admin accounts.

    As well as this model is connected with `User` through one2one relationship,
    this model can also be used to mention all admin users.
    """

    account = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        primary_key=True,
        related_name="options_admin",
    )

    class Meta:
        verbose_name = "Параметры администратора"
        verbose_name_plural = "Параметры администраторов"
