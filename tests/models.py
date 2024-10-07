from django.db import models
from django_peeringdb.models import LG_URLField, MultipleChoiceField, URLField


class FieldModel(models.Model):
    url = URLField(null=True, blank=True)
    multichoice = MultipleChoiceField(
        max_length=255,
        null=True,
        blank=True,
        choices=[("1", "1"), ("2", "2"), ("3", "3")],
    )

    class Meta:
        app_label = "django_peeringdb.tests"


class LG_FieldModel(models.Model):
    url = LG_URLField(null=True, blank=True)

    class Meta:
        app_label = "django_peeringdb.tests"
