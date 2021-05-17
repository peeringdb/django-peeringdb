from django.core.exceptions import ValidationError
from django.test import TestCase
import ipaddress
import pytest

from django_peeringdb.models import (
    URLField,
    LG_URLField,
)
from tests.models import FieldModel, LG_FieldModel


class FieldTests(TestCase):
    """test model functionality"""

    def test_init(self):
        new = URLField()

    def test_url(self):
        model = FieldModel()

        model.url = "http://example.com"
        model.full_clean()

        model.url = "https://example.com"
        model.full_clean()

        with pytest.raises(ValidationError):
            model.url = "invalid"
            model.full_clean()


class LG_FieldTests(TestCase):
    """test model functionality"""

    def test_init(self):
        new = LG_URLField()

    def test_url(self):
        model = LG_FieldModel()

        model.url = "telnet://example.com"
        model.full_clean()

        model.url = "ssh://user@example.com"
        model.full_clean()

        with pytest.raises(ValidationError):
            model.url = "invalid"
            model.full_clean()
