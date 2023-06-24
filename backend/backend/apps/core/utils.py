from django.forms.fields import MultipleChoiceField
from django_filters.filters import Filter
from enum import Enum


class MultipleValueField(MultipleChoiceField):
    """MultipleChoiceField with custom validation."""

    def __init__(self, *args, field_class, **kwargs):
        """Initialize `MultipleChoiceField` with custom `field_class`."""
        self.inner_field = field_class()
        super().__init__(*args, **kwargs)

    def valid_value(self, value):
        """Validate using `Field` class passed to a constructor."""
        return self.inner_field.validate(value)

    def clean(self, values):
        """Clean values using `Field` class passed to a constructor."""
        return values and [self.inner_field.clean(value) for value in values]


class MultipleValueFilter(Filter):
    """Custom filter for django-filter that allows filtering by multiple values."""

    field_class = MultipleValueField

    def __init__(self, *args, field_class, **kwargs):
        """Initialize `MultipleValueField` with custom `field_class`."""
        kwargs.setdefault("lookup_expr", "in")
        super().__init__(*args, field_class=field_class, **kwargs)


class OrderStatus(Enum):
    opened = 1
    cooking = 2
    witing_delivery = 3
    on_the_way = 4
    closed = 5


class DeliveryManStatus(Enum):
    ready = 1
    busy = 2
    at_home = 3


ORDER_TYPE_CHOICES = (
    (OrderStatus.opened.value, "Открыт"),
    (OrderStatus.cooking.value, "Готовится"),
    (OrderStatus.on_the_way.value, "В пути"),
    (OrderStatus.closed.value, "Закрыт"),
    (OrderStatus.witing_delivery.value, "Ждет курьера"),
)

DELIVERYMAN_TYPE_CHOICES = (
    (DeliveryManStatus.ready.value, "Свободен"),
    (DeliveryManStatus.busy.value, "Доставляет"),
    (DeliveryManStatus.at_home.value, "Не на смене"),
)
