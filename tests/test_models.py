import pytest
from django.core.exceptions import ValidationError
from django.test import TestCase
from django_peeringdb.models import LG_URLField, URLField

from tests.models import FieldModel, LG_FieldModel


class FieldTests(TestCase):
    """test model functionality"""

    def test_init(self):
        URLField()

    def test_url(self):
        model = FieldModel()

        model.url = "http://example.com"
        model.full_clean()

        model.url = "https://example.com"
        model.full_clean()

        with pytest.raises(ValidationError):
            model.url = "invalid"
            model.full_clean()

    def test_multichoice(self):
        model = FieldModel()

        model.multichoice = ["1", "2"]
        model.full_clean()

        model.multichoice = "1"
        model.full_clean()
        assert model.multichoice == ["1"]

        with pytest.raises(ValidationError):
            model.multichoice = ["4"]
            model.full_clean()

        with pytest.raises(ValidationError):
            model.multichoice = "4"
            model.full_clean()

    def test_multichoice_to_python(self):
        model = FieldModel()
        field = model._meta.get_field("multichoice")
        field.to_python("") is None
        field.to_python("[]") is None
        field.to_python("1,2,3") == ["1", "2", "3"]
        field.to_python(["1", "2", "3"]) == ["1", "2", "3"]


class LG_FieldTests(TestCase):
    """test model functionality"""

    def test_init(self):
        LG_URLField()

    def test_url(self):
        model = LG_FieldModel()

        model.url = "telnet://example.com"
        model.full_clean()

        model.url = "ssh://user@example.com"
        model.full_clean()

        with pytest.raises(ValidationError):
            model.url = "invalid"
            model.full_clean()
