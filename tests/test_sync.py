
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
from django_peeringdb import settings


def sync_test(f):
    """
    check for sync settings, configure
    return decorator for all tests that sync
    """
    sync = pytest.config.getoption("--sync")

    # check explicitly for False, none means default (which is prod)
    if sync == False:
        return pytest.mark.skip(reason="need --sync option to run sync tests")(f)

    f.sync_args = dict(
        debug=pytest.config.getoption('--sync-debug'),
        )

    sync_only = pytest.config.getoption("--sync-only")
    if sync_only:
        f.sync_args['only'] = sync_only

    sync_id = pytest.config.getoption("--sync-id")
    if sync_id:
        f.sync_args['id'] = sync_id

    if not sync or sync == 'prod':
        pass

    elif sync == 'beta':
        settings.SYNC_URL = 'https://beta.peeringdb.com/api'

    else:
        settings.SYNC_URL = sync


    return f


@sync_test
class SyncTests(TestCase):
    """ test sync command """

    def setUp(self):
        self.cmd = load_command_class('django_peeringdb', 'pdb_sync')

    def test_get_since_empty(self):
        for cls in self.cmd.get_class_list():
            if cls.handleref.tag == "poc":
                continue
            assert 0 == self.cmd.get_since(cls)

    def test_sync_all(self):
        kwargs = getattr(self, 'sync_args', {})
        print("syncing kwargs {}".format(kwargs))
        self.cmd.handle(**kwargs)
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

