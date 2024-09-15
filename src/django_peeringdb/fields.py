import django.forms
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


class MultipleChoiceField(models.CharField):
    """
    Field that can take a set of string values
    and store them in a charfield using a delimiter

    This needs to be compatible with django-rest-framework's
    multiple choice field.
    """

    def cleaned_values(self, values):
        return [value.strip("{}' ") for value in values]

    def clean_choices(self, values):
        for value in values:
            exists = False
            for choice, label in self.choices:
                if choice == value:
                    exists = True
                    break

            if not exists:
                raise ValidationError(_("Invalid value: {}").format(value))

    def validate(self, value, model_instance):
        if not self.editable:
            # Skip validation for non-editable fields.
            return

        self.clean_choices(self.cleaned_values(value))

        if value is None and not self.null:
            raise ValidationError(self.error_messages["null"], code="null")

        if not self.blank and value in self.empty_values:
            raise ValidationError(self.error_messages["blank"], code="blank")

    def from_db_value(self, value, expression, connection):
        if value is None:
            return None

        if not value or value == "[]":
            return []

        values = self.cleaned_values(value.split(","))

        self.clean_choices(values)

        return values

    def get_prep_value(self, value):
        if value is None:
            return ""

        picked = []
        for choice, label in self.choices:
            if choice in value:
                picked.append(choice)

        return ",".join(picked)

    def to_python(self, value):
        if isinstance(value, (list, set, tuple)):
            return value

        if not value or value == "[]":
            return None

        values = self.cleaned_values(value.split(","))
        self.clean_choices(values)

        return values

    def formfield(self, **kwargs):
        defaults = {"form_class": django.forms.MultipleChoiceField}
        defaults.update(**kwargs)
        return super().formfield(**defaults)

    def value_to_string(self, obj):
        values = self.value_from_object(obj)
        self.clean_choices(self.cleaned_values(values))
        return ",".join(values)
