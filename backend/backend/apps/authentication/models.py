from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone


from .manager import UserManager
from .utils import ACCOUNT_TYPE_CHOICES, UserTypes


class User(AbstractBaseUser, PermissionsMixin):
    """User model."""

    email = models.EmailField("Почта", unique=True)
    account_type = models.IntegerField(
        "Тип аккаунта", default=UserTypes.STUDENT, choices=ACCOUNT_TYPE_CHOICES
    )
    is_active = models.BooleanField("Активный", default=True)
    is_staff = models.BooleanField("Администратор", default=False)
    first_name = models.CharField("Имя", max_length=100)
    last_name = models.CharField("Отчество", max_length=100, blank=True, default="")
    surname = models.CharField("Фамилия", max_length=100)
    date_joined = models.DateTimeField("Дата регистрации", default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["account_type", "first_name", "surname"]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        permissions = [("edit_news", "Может редактировать статьи в новостном блоке.")]

    def get_full_name(self):
        """Get a full name of a user (surname, first name & second name)."""
        return f"{self.surname} {self.first_name} {self.last_name}"

    def get_short_name(self):
        """Get a short name of a user (surname and first name)."""
        return f"{self.surname} {self.first_name}"

    def get_username(self):
        """Get a user's email."""
        return self.email

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to a user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def is_student(self) -> bool:
        """Check if user's a student."""
        return self.account_type == UserTypes.STUDENT

    @property
    def is_teacher(self) -> bool:
        """Check if user's a teacher."""
        return self.account_type == UserTypes.TEACHER

    @property
    def is_admin(self) -> bool:
        """Check if user's an admin."""
        return self.account_type in [UserTypes.ROOT, UserTypes.ADMIN]

    def __str__(self):
        return self.get_username()


class Teacher(models.Model):
    """
    User options for teacher accounts.

    As well as this model is connected with `User` through one2one relationship,
    this model can also be used to mention all teacher users.
    """

    account = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="options_teacher",
        verbose_name="Пользователь",
        primary_key=True,
    )
    # TODO: Add subjects field
    # subjects = models.ManyToManyField("Subjects", verbose_name="Предметы")

    class Meta:
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"

    def __str__(self):
        return "{}".format(self.account.get_full_name())


class Student(models.Model):
    """
    Options for student accounts.

    As well as this model is connected with `User` through one2one relationship,
    this model can also be used to mention all student users.
    """

    account = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        primary_key=True,
        related_name="options_student",
    )

    klass = models.ForeignKey(
        "core.Klass",
        on_delete=models.SET_NULL,
        null=True,
        default=None,
        verbose_name="Класс",
        blank=True,
    )

    is_monitor = models.BooleanField(verbose_name="Староста", default=False)

    class Meta:
        # ordering = ["klass"]
        verbose_name = "Ученик"
        verbose_name_plural = "Ученики"

    def __str__(self):
        # TODO: Show student's klass in __str__
        return "{}".format(self.account.get_short_name())


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
