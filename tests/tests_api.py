import unittest

import steampi.api


class TestApiMethods(unittest.TestCase):
    def test_get_appdetails_url(self):
        app_id = '440'
        expected_url = 'https://store.steampowered.com/api/appdetails?appids=' + str(app_id)
        self.assertEqual(steampi.api.get_appdetails_url(app_id), expected_url)

    def test_download_app_details(self):
        app_id = '440'
        (_, is_success, _) = steampi.api.download_app_details(app_id)
        self.assertTrue(is_success)

    def test_get_appdetails_filename(self):
        app_id = '440'
        expected_filename = 'data/appdetails/appID_' + str(app_id) + '.json'
        self.assertEqual(steampi.api.get_appdetails_filename(app_id), expected_filename)

    def test_load_app_details(self):
        app_id = '440'
        (_, is_success, _) = steampi.api.load_app_details(app_id)
        self.assertTrue(is_success)


if __name__ == '__main__':
    unittest.main()
