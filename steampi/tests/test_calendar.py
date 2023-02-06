import unittest

import steampi


class TestCalendarMethods(unittest.TestCase):
    def test_get_release_date_as_str(self):
        app_id = '440'
        release_date = steampi.get_release_date_as_str(app_id)
        assert release_date == '10 Oct, 2007' or release_date == 'Oct 10, 2007'

    def test_get_release_date_as_datetime(self):
        app_id = '440'
        release_date = steampi.get_release_date_as_datetime(app_id)
        assert release_date.year == 2007
        assert release_date.month == 10
        assert release_date.day == 10

    def test_get_release_year(self):
        app_id = '440'
        release_year = steampi.get_release_year(app_id)
        assert release_year == 2007


if __name__ == '__main__':
    unittest.main()
