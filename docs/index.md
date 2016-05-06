
# Django PeeringDB

## Installation

    pip install django-peeringdb

Then add `django_peeringdb` to INSTALLED_APPS

## Models
Both Abstract and Concrete models are defined, if you want to extend the models in your own application, you'd want to add `PEERINGDB_ABSTRACT_ONLY=True` to your settings file. Please be sure to add the required `ForeignKey` columns to your models, check `models/concrete.py` for the needed relationships.


## Settings

!!! danger "Required Settings"

            COUNTRIES_OVERRIDE={
               'XK': _('Kosovo'),
            },

    If you're not using _ for tranlastions, add:

        _ = lambda s: s

    or remove `_()`

#### PEERINGDB_TABLE_PREFIX
default `'peeringdb_'`
Prefix all table names with this

#### PEERINGDB_ABSTRACT_ONLY
default `False`
Only load abstract models

#### PEERINGDB_SYNC_URL
default `'https://www.peeringdb.com/api'`
PeeringDB API endpoint URL

#### PEERINGDB_SYNC_USERNAME
default `''`
PeeringDB username

#### PEERINGDB_SYNC_PASSWORD
default `''`
PeeringDB password

#### PEERINGDB_SYNC_STRIP_TZ
default `False`
Strip timezone from datetime fields, useful for databases that don't support timezones, such as sqlite3

#### PEERINGDB_SYNC_ONLY
default `[]`
Only sync these tables

## Commands

#### pdb_sync
    python manage.py pdb_sync

Will sync the full peeringdb database to your models, any subsequent call will only sync records that have changed.

