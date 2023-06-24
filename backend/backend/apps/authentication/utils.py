from enum import Enum


class UserTypes(Enum):
    """User types."""

    ROOT = 0
    ADMIN = 1
    DELIVER = 2


ACCOUNT_TYPE_CHOICES = (
    (UserTypes.ROOT.value, "Root"),
    (UserTypes.ADMIN.value, "Администратор"),
    (UserTypes.DELIVER.value, "Доставчик"),
)
