from enum import Enum


class UserTypes(Enum):
    """User types."""

    ROOT = 0
    ADMIN = 1
    TEACHER = 2
    STUDENT = 3


ACCOUNT_TYPE_CHOICES = (
    (UserTypes.ROOT.value, "Root"),
    (UserTypes.ADMIN.value, "Администратор"),
    (UserTypes.TEACHER.value, "Учитель"),
    (UserTypes.STUDENT.value, "Ученик"),
)
