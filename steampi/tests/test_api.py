import unittest

import steampi


class TestApiMethods(unittest.TestCase):
    def test_get_appdetails_url(self):
        app_id = '440'
        expected_url = 'https://store.steampowered.com/api/appdetails?appids=' + str(app_id)
        self.assertEqual(steampi.get_appdetails_url(app_id), expected_url)

    def test_download_app_details(self):
        app_id = '440'
        (_, is_success, _) = steampi.download_app_details(app_id)
        self.assertTrue(is_success)

    def test_get_appdetails_filename(self):
        app_id = '440'
        expected_filename = 'data/appdetails/appID_' + str(app_id) + '.json'
        self.assertEqual(steampi.get_appdetails_filename(app_id), expected_filename)

    def test_load_app_details(self):
        app_id = '440'
        (_, is_success, _) = steampi.load_app_details(app_id)
        self.assertTrue(is_success)


if __name__ == '__main__':
    unittest.main()
