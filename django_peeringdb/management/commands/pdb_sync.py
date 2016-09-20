"""
sync peeringdb tables
"""
from __future__ import print_function

import logging
import re
from optparse import make_option
import time
from twentyc.rpc import RestClient

import django.core.exceptions
from django.core.management.base import BaseCommand, CommandError
from django_peeringdb import settings, sync

import django_peeringdb.models
from django_peeringdb.models.concrete import (
  Organization,
  Network,
  InternetExchange,
  Facility,
  NetworkContact,
  NetworkIXLan,
  NetworkFacility,
  IXLan,
  InternetExchangeFacility
)

from django.apps import apps


def get_model(name):
    return apps.get_model('django_peeringdb', name)


class Command(BaseCommand):
    help = "synchronize local tables to PeeringDB"

    option_list = BaseCommand.option_list + (
        make_option('-n', '--dry-run',
            action='store_true',
            default=False,
            help='enable extra debug output'),
        make_option('--debug',
            action='store_true',
            default=False,
            help='enable extra debug output'),
        make_option('--only',
            action='store',
            default=False,
            help='only process this ixp (id)'),
        )
# progress
# quiet

    def handle(self, *args, **options):
        self.log = logging.getLogger('peeringdb.sync')

        kwargs = {}
        if settings.SYNC_USERNAME:
            kwargs['user'] = settings.SYNC_USERNAME
            kwargs['password'] = settings.SYNC_PASSWORD

        self.connect(settings.SYNC_URL, **kwargs)

        # get models if limited by config
        tables = self.get_class_list(settings.SYNC_ONLY)

        # disable auto now
        for model in tables:
            for field in model._meta.fields:
                if field.name == "created":
                    field.auto_now_add = False
                if field.name == "updated":
                    field.auto_now = False

        self.sync(tables)

    def connect(self, url, **kwargs):
        self.rpc = RestClient(url, **kwargs)

    def sync(self, tables):
        for cls in tables:
            self.update_db(cls, self.get_objs(cls))

    def get_class_list(self, only=None):
        tables = []
        if only:
            for name in only:
                tables.append(get_model(name))
        else:
            tables = django_peeringdb.models.all_models
        return tables

    def get_since(self, cls):
        upd = cls.handleref.last_change()
        if upd:
            return int(time.mktime(upd.timetuple()))
        return 0

    def get_data(self, cls, since):
        return self.rpc.all(cls._handleref.tag, since=since)

    def get_objs(self, cls, **kwargs):
        since = self.get_since(cls)

        data = self.rpc.all(cls._handleref.tag, since=since, **kwargs)
        #data = self.rpc.all(cls._handleref.tag, since=since, limit=20)
        print("%s last update %s %d changed" % (cls._handleref.tag, str(since), len(data)))
        #print(data)
        return data

    def cls_from_tag(self, tag):
        tables = self.get_class_list()
        for cls in tables:
            if cls._handleref.tag == tag:
                return cls
        raise Exception("Unknown reftag: %s" % tag)

    def _sync(self, cls, row):
        """
        Try to sync an object to the local database, in case of failure
        where a referenced object is not found, attempt to fetch said 
        object from the REST api
        """
        try:
            sync.sync_obj(cls, row)
        except django.core.exceptions.ValidationError, inst:
           # There were validation errors
           for field, errlst in inst.error_dict.items():
                # check if it was a relationship that doesnt exist locally
                m = re.match(".+ with id (\d+) does not exist.+", str(errlst))
                if m:
                    print("%s.%s not found locally, trying to fetch object... " % (field, m.group(1)))
                    # fetch missing object
                    r = self.rpc.get(field, int(m.group(1)), depth=0)

                    # sync missing object
                    self._sync(self.cls_from_tag(field), r[0])
                else:
                    raise
           
           # try to sync initial object once more
           sync.sync_obj(cls, row)

    def update_db(self, cls, data):
        print("data to be processed", len(data))
        if not data:
            return

        for row in data:
            self._sync(cls, row)

