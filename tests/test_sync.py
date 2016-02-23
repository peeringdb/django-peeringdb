
import datetime
import pytest

from django.utils.timezone import make_naive
from django.core.management import (
    call_command,
    find_commands,
    load_command_class,
)
from django.test import TestCase
import django_peeringdb.models


class SyncTests(TestCase):
    """ test sync command """

    def setUp(self):
        self.cmd = load_command_class('django_peeringdb', "pdb_sync")

    def test_get_since_empty(self):
        for cls in self.cmd.get_class_list():
            if cls.handleref.tag == "poc":
                continue
            assert 0 == self.cmd.get_since(cls)

    def test_sync_all(self):
        self.cmd.handle()
#        self.cmd.sync(self.cmd.get_class_list())

#        for cls in self.cmd.get_class_list():
#            data = self.cmd.get_objs(cls)
#            for row in data:
#                for field in cls._meta.get_fields():
#                    value = cls._meta.get_field(field.name)
#                    if isinstance(value, datetime.datetime):
#                        #cls._meta.get_field(field.name).make_naive()
#                        setattr(cls, field.name, make_naive(value))
#
#            self.cmd.update_db(cls, data)
#
#            self.update_db(cls, self.get_objs(cls))

        for cls in self.cmd.get_class_list():
            if cls.handleref.tag == "poc":
                continue
            assert 0 != self.cmd.get_since(cls)
            assert 0 != cls.objects.all().count()
            print(cls.objects.all().count())

