
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


class CoreTests(TestCase):
    """ test core functionality """

    def setUp(self):
        self.cmd = load_command_class('django_peeringdb', "pdb_sync")

    def test_get_class_list(self):
        models = self.cmd.get_class_list()
        assert len(models)
        assert django_peeringdb.models.all_models == models

        models = self.cmd.get_class_list(['network'])
        assert 1 == len(models)
        assert models[0] == django_peeringdb.models.Network

    def test_get_tag_dict(self):
        tag_dict = django_peeringdb.models.tag_dict
        assert len(tag_dict)
        for k,v in tag_dict.items():
            assert k == v._handleref.tag

