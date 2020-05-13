# mock backend classes from peeringdb-py client

from django_peeringdb.models import all_models


def reftag_to_cls(fn):
    return fn


class Resource(object):
    def __init__(self, tag):
        self.tag = tag


class Interface(object):
    REFTAG_RESOURCE = dict(
        [(model.HandleRef.tag, Resource(model.HandleRef.tag)) for model in all_models]
    )

    def get_resource(self, concrete):
        return self.REFTAG_RESOURCE[concrete.HandleRef.tag]
