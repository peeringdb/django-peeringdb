from django.db import models
from django_peeringdb.models import URLField, LG_URLField


class FieldModel(models.Model):
    url = URLField(null=True, blank=True)

    class Meta:
        app_label = "django_peeringdb.tests"


class LG_FieldModel(models.Model):
    url = LG_URLField(null=True, blank=True)

    class Meta:
        app_label = "django_peeringdb.tests"
