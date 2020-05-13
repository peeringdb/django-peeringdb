# PeeringDB client backend implementation module

import re
import calendar
from decimal import Decimal
from ipaddress import IPv4Address, IPv6Address
from collections import defaultdict

import django
from django.apps import apps
from django.conf import settings
from django.core.exceptions import (
    ValidationError,
    FieldDoesNotExist,
    ObjectDoesNotExist,
)
from django.core.management import call_command
from django.db import models, connections, DEFAULT_DB_ALIAS, IntegrityError, connection
from django.db.migrations.executor import MigrationExecutor
from django.db.transaction import atomic as atomic_transaction

from django_countries.fields import Country

import django_peeringdb.models
from django_peeringdb import __version__
from django_peeringdb.models import concrete

from peeringdb import resource
from peeringdb.backend import reftag_to_cls, Interface


class Backend(Interface):

    # Non-builtin scalar types
    CUSTOM_FIELDS = (
        Decimal,
        Country,
        IPv4Address,
        IPv6Address,
    )

    # Resource (abstract) and model (concrete) definitions
    RESOURCE_MAP = {
        resource.Facility: concrete.Facility,
        resource.InternetExchange: concrete.InternetExchange,
        resource.InternetExchangeFacility: concrete.InternetExchangeFacility,
        resource.InternetExchangeLan: concrete.IXLan,
        resource.InternetExchangeLanPrefix: concrete.IXLanPrefix,
        resource.Network: concrete.Network,
        resource.NetworkContact: concrete.NetworkContact,
        resource.NetworkFacility: concrete.NetworkFacility,
        resource.NetworkIXLan: concrete.NetworkIXLan,
        resource.Organization: concrete.Organization,
    }

    ERROR_PATTERNS = {
        "mysql": {
            "unique": [(r"Duplicate entry '[^\']+' for key '(?P<field_name>\w+)'", 1)],
        },
        "sqlite": {
            "unique": [
                (r"UNIQUE constraint failed: (\w+)\.(?P<field_name>\w+)", 0),
                (r"column (?P<field_name>\w+) is not unique", 0),
            ],
        },
    }

    @classmethod
    def setup(cls):
        # in order to copy updated / created times from server
        # we need to turn off auto updating of those fields
        # during update and add
        for model in django_peeringdb.models.all_models:
            for field in model._meta.fields:
                if field.name in ["created", "updated"]:
                    field.auto_now_add = False
                    field.auto_now = False

    @classmethod
    def atomic_transaction(cls):
        return atomic_transaction()

    @classmethod
    def validation_error(cls, concrete=None):
        return ValidationError

    @classmethod
    def object_missing_error(cls, concrete=None):
        if concrete:
            return concrete.DoesNotExist
        return ObjectDoesNotExist

    @reftag_to_cls
    def last_change(self, concrete):
        upd = concrete.handleref.last_change()
        if upd:
            return int(calendar.timegm(upd.timetuple()))
        return 0

    @reftag_to_cls
    def get_object(self, concrete, id):
        return concrete.objects.get(pk=id)

    @reftag_to_cls
    def get_object_by(self, concrete, field_name, value):
        return concrete.objects.get(**{field_name: value})

    @reftag_to_cls
    def get_objects(self, concrete, ids=None):
        if ids:
            return concrete.objects.filter(pk__in=ids)
        return concrete.objects.all()

    @reftag_to_cls
    def get_objects_by(self, concrete, field_name, value):
        return concrete.objects.filter(**{field_name: value})

    @reftag_to_cls
    def create_object(self, concrete, **data):
        return concrete.objects.create(**data)

    @reftag_to_cls
    def get_fields(self, concrete):
        return concrete._meta.get_fields()

    @reftag_to_cls
    def get_field(self, concrete, field_name):
        return concrete._meta.get_field(field_name)

    @reftag_to_cls
    def get_field_concrete(self, concrete, field_name):
        return concrete._meta.get_field(field_name).related_model

    @reftag_to_cls
    def is_field_related(self, concrete, field_name):
        field = self.get_field(concrete, field_name)
        related = getattr(field, "related_model", False)
        multiple = getattr(field, "multiple", False)
        return (related, multiple)

    def set_relation_many_to_many(self, obj, field_name, objs):
        "Set a many-to-many field on an object"
        relation = getattr(obj, field_name)
        if hasattr(relation, "set"):
            relation.set(objs)  # Django 2.x
        else:
            setattr(obj, field_name, objs)  # Django 1.x

    def clean(self, obj):
        obj.full_clean()

    def save(self, obj):
        obj.save()

    def convert_field(self, concrete, field_name, value):
        field = concrete._meta.get_field(field_name)
        if isinstance(field, models.DecimalField) and isinstance(value, float):
            return Decimal("{:.{prec}f}".format(value, prec=field.decimal_places))
        else:
            return value

    def detect_missing_relations(self, obj, exc):
        """
        Parse error messages and collect the missing-relationship errors
        as a dict of Resource -> {id set}
        """
        missing = defaultdict(set)
        for name, err in list(exc.error_dict.items()):
            # check if it was a relationship that doesnt exist locally
            pattern = r".+ with id (\d+) does not exist.+"
            m = re.match(pattern, str(err))
            if m:
                field = obj._meta.get_field(name)
                res = self.get_resource(field.related_model)
                missing[res].add(int(m.group(1)))
        return missing

    def detect_uniqueness_error(self, exc):
        """
        Parse error, and if it describes any violations of a uniqueness constraint,
        return the corresponding fields, else None
        """
        pattern = r"(\w+) with this (\w+) already exists"

        fields = []
        if isinstance(exc, IntegrityError):
            return self._detect_integrity_error(exc)
        assert isinstance(exc, ValidationError), TypeError

        for name, err in list(exc.error_dict.items()):
            if re.search(pattern, str(err)):
                fields.append(name)
        return fields or None

    def _detect_integrity_error(self, exc):

        engine = connection.vendor
        patterns = self.ERROR_PATTERNS[engine]

        fields = []
        assert isinstance(exc, IntegrityError)
        # for name, err in exc.error_dict.items():
        for pattern, index in patterns.get("unique"):
            m = re.search(pattern, str(exc.args[index]))
            if m:
                return [m.groupdict()["field_name"]]
        return None

    # Database
    def migrate_database(self, verbosity=0):
        call_command("migrate", interactive=False, verbosity=verbosity)

    # credit to https://stackoverflow.com/a/31847406/1325447
    def is_database_migrated(self, database=DEFAULT_DB_ALIAS):
        connection = connections[database]
        connection.prepare_database()
        executor = MigrationExecutor(connection)
        targets = executor.loader.graph.leaf_nodes()
        # No plan <=> Yes sync'd
        return not executor.migration_plan(targets)

    def delete_all(self):
        call_command("flush", interactive=False, verbosity=1)
