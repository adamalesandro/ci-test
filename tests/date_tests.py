import unittest
import datetime
from sgnl import dates


class DateTest(unittest.TestCase):

    def test_to_mmddyy(self):
        d = datetime.datetime(2015, 03, 31)
        return self.assertEqual(dates.to_mmddyy(d), "033115")

    def test_prev_weekday(self):
        d = datetime.datetime(2015, 03, 31)
        prev_d = datetime.datetime(2015, 03, 30)

        return self.assertEquals(dates.prev_weekday(d), prev_d)

