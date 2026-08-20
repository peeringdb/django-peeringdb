import pytest
from django import forms
from django.core.exceptions import ValidationError
from django.test import TestCase

from django_peeringdb.models import LG_URLField, MultipleChoiceField, URLField
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
        field = FieldModel._meta.get_field("multichoice")
        assert field.to_python("") is None
        assert field.to_python("[]") is None
        assert field.to_python("1,2,3") == ["1", "2", "3"]
        assert field.to_python(["1", "2", "3"]) == ["1", "2", "3"]
        assert field.to_python(("1", "2")) == ("1", "2")

    def test_multichoice_cleaned_values(self):
        field = FieldModel._meta.get_field("multichoice")
        # strips surrounding braces, quotes and whitespace
        assert field.cleaned_values(["{1}", " 2 ", "'3'"]) == ["1", "2", "3"]

    def test_multichoice_clean_choices(self):
        field = FieldModel._meta.get_field("multichoice")
        field.clean_choices(["1", "2"])  # valid choices -> no error
        with pytest.raises(ValidationError):
            field.clean_choices(["9"])  # not a valid choice

    def test_multichoice_from_db_value(self):
        field = FieldModel._meta.get_field("multichoice")
        assert field.from_db_value(None, None, None) is None
        assert field.from_db_value("", None, None) == []
        assert field.from_db_value("[]", None, None) == []
        assert field.from_db_value("1,2", None, None) == ["1", "2"]

    def test_multichoice_get_prep_value(self):
        field = FieldModel._meta.get_field("multichoice")
        assert field.get_prep_value(None) == ""
        assert field.get_prep_value([]) == ""
        assert field.get_prep_value(["1", "3"]) == "1,3"

    def test_multichoice_value_to_string(self):
        field = FieldModel._meta.get_field("multichoice")
        model = FieldModel()
        model.multichoice = ["1", "2"]
        assert field.value_to_string(model) == "1,2"

    def test_multichoice_validate_editable_and_blank(self):
        # non-editable field: validate short-circuits and ignores the value
        non_editable = MultipleChoiceField(editable=False, choices=[("1", "1")])
        non_editable.validate(["9"], None)  # invalid value tolerated (not editable)

        # blank not allowed + empty value -> ValidationError
        non_blank = MultipleChoiceField(blank=False, null=True, choices=[("1", "1")])
        with pytest.raises(ValidationError):
            non_blank.validate([], None)

    def test_multichoice_formfield(self):
        # NOTE: because the field defines `choices`, Django's Field.formfield
        # selects `choices_form_class` (TypedChoiceField) over the form_class
        # this method sets; assert the actual returned form-field base.
        field = FieldModel._meta.get_field("multichoice")
        assert isinstance(field.formfield(), forms.ChoiceField)


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
