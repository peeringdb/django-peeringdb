
# django-peeringdb

[![PyPI](https://img.shields.io/pypi/v/django_peeringdb.svg?maxAge=2592000)](https://pypi.python.org/pypi/django_peeringdb)
[![PyPI](https://img.shields.io/pypi/pyversions/django-peeringdb.svg)](https://pypi.python.org/pypi/django-peeringdb)
[![Tests](https://github.com/peeringdb/django-peeringdb/workflows/tests/badge.svg)](https://github.com/peeringdb/django-peeringdb/actions/workflows/tests.yml)
[![Codecov](https://img.shields.io/codecov/c/github/peeringdb/django-peeringdb/master.svg?maxAge=2592000)](https://codecov.io/github/peeringdb/django-peeringdb)


**Django models for PeeringDB.**

This package provides Django-native models and admin support for working with PeeringDB data. It is used by both the [PeeringDB web application (`peeringdb_server`)](https://github.com/peeringdb/peeringdb) and the [PeeringDB CLI client (`peeringdb-py`)](https://github.com/peeringdb/peeringdb-py). It enables direct access to PeeringDB objects via Django’s ORM and admin UI.

While the models are defined here, synchronization of PeeringDB data is handled by the external [`peeringdb` CLI](https://github.com/peeringdb/peeringdb-py) tool.

---

### Synchronizing PeeringDB Data

Synchronization logic has been moved out of `django-peeringdb` and into the standalone [`peeringdb` CLI](https://github.com/peeringdb/peeringdb-py) tool. This decouples data sync from your application and provides a consistent way to keep PeeringDB data up to date across different environments.

For more detailed information, refer to the [peeringdb CLI documentation](https://github.com/peeringdb/peeringdb-py/tree/master/docs)




See the docs at http://peeringdb.github.io/django-peeringdb/

