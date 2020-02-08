from django.test import TestCase
from django.utils.dateparse import parse_datetime
from django.utils.timezone import make_aware, make_naive, utc


class TimeZoneTests(TestCase):
    """ test time zone handling """

    def test_conversion(self):
        input = "2020-02-04T20:34:14Z"
        parsed = parse_datetime(input)

        assert parsed.year == 2020
        assert parsed.month == 2
        assert parsed.day == 4
        assert parsed.hour == 20
        assert parsed.minute == 34
        assert parsed.utcoffset().seconds == 0

        stripped = parsed.replace(tzinfo=None)

        assert stripped.year == 2020
        assert stripped.month == 2
        assert stripped.day == 4
        assert stripped.hour == 20
        assert stripped.minute == 34
        assert stripped.utcoffset() is None

        aware = make_aware(stripped)

        assert aware.year == 2020
        assert aware.month == 2
        assert aware.day == 4
        assert aware.hour == 20
        assert aware.minute == 34
        assert aware.utcoffset().seconds == 0

        naive = make_naive(aware, timezone=utc)

        assert naive.year == 2020
        assert naive.month == 2
        assert naive.day == 4
        assert naive.hour == 20
        assert naive.minute == 34
        assert naive.utcoffset() is None
