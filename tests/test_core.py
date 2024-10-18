import django_peeringdb.models
from django.test import TestCase


class CoreTests(TestCase):
    """test core functionality"""

    def test_tag_dict(self):
        tag_dict = django_peeringdb.models.tag_dict
        assert len(tag_dict)
        for k, v in list(tag_dict.items()):
            assert k == v._handleref.tag
