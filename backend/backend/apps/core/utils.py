from django.forms.fields import MultipleChoiceField

from django_filters.filters import Filter


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
