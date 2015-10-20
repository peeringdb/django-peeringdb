
# Django PeeringDB

## Settings

#### PEERINGDB_TABLE_PREFIX
default `'peeringdb_'`
Prefix all table names with this

#### PEERINGDB_ABSTRACT_ONLY
default `False`
Only load abstract models

#### PEERINGDB_SYNC_URL
default `'https://beta.peeringdb.com/api'`
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

