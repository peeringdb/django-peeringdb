
import datetime
from django.core.exceptions import ValidationError
from django.db import models
from django_peeringdb import settings
import logging


def sync_obj(cls, row):
    try:
        obj = cls.objects.get(pk=row['id'])

    except cls.DoesNotExist:
        obj = cls()
        #obj = cls(**row)

    for k, v in row.items():
        setattr(obj, k, v)

    try:
        obj.full_clean()

    except ValidationError as e:
        log = logging.getLogger('peeringdb.sync')
        log.debug("{} : errors: {}".format(e, e.message_dict))
        for k, v in e.message_dict.items():
            field = cls._meta.get_field(k)
            log.debug("{}: {}, dict: {}".format(k, getattr(obj, k), field.__dict__))
        raise


    for field in cls._meta.get_fields():
        ftyp = cls._meta.get_field(field.name)
        value = getattr(obj, field.name, None)
        if settings.SYNC_STRIP_TZ and isinstance(value, datetime.datetime):
            setattr(obj, field.name, value.replace(tzinfo=None))
        else:
            if hasattr(ftyp, "related_name") and ftyp.multiple:
                continue
            else:
                setattr(obj, field.name, value)

    obj.save()
    return

    # times should always be UTC, so take off timezone since some dbs
    # don't support it - FIXME make option
    for field in cls._meta.get_fields():
        #if isinstance(field, models.ForeignKey):
        if isinstance(field, models.ForeignKey):
            key = field.name + "_id"
            value = getattr(obj, key, 0)
        else:
            key = field.name
            value = getattr(obj, field.name, None)

        if isinstance(value, datetime.datetime):
            setattr(obj, field.name, value.replace(tzinfo=None))
        else:
            setattr(obj, field.name, value)

    return
