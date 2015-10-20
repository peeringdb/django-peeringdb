
import datetime
from django.db import models
from django_peeringdb import settings

#>>> from django.apps import apps
#>>> User = apps.get_model(app_label='auth', model_name='User')



#def get_last_update(table):

def sync_obj(cls, row):
    try:
        obj = cls.objects.get(pk=row['id'])

    except cls.DoesNotExist:
        obj = cls()
        #obj = cls(**row)

    for k, v in row.items():
#        field = cls._meta.get_field(k)
        setattr(obj, k, v)

    obj.full_clean()

    for field in cls._meta.get_fields():
        ftyp = cls._meta.get_field(field.name)
        value = getattr(obj, field.name, None)
        if settings.SYNC_STRIP_TZ and isinstance(value, datetime.datetime):
            setattr(obj, field.name, value.replace(tzinfo=None))
        else:
            #print field.name #, "is related", field.is_related
            #print vars(field)
            #print "ftyp", vars(ftyp)
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
