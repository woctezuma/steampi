import unittest

import steampi


class TestJsonUtilsMethods(unittest.TestCase):

    def test_get_data_path(self):
        self.assertEqual(steampi.get_data_path(), 'data/')

    def test_download_json_data(self):
        app_id = '440'
        url = 'https://store.steampowered.com/api/appdetails?appids=' + str(app_id)
        _, status_code = steampi.download_json_data(url, verbose=True)
        self.assertTrue(status_code == 200)

    def test_save_json_data(self):
        json_filename = 'unit_test.json'
        json_data = {'hello, world': 37, 'hello, universe': 42}
        self.assertTrue(steampi.save_json_data(json_filename, json_data))

    def test_load_json_data(self):
        json_filename = 'unit_test.json'
        json_data = {'hello, world': 37, 'hello, universe': 42}
        steampi.save_json_data(json_filename, json_data)
        loaded_data = steampi.load_json_data(json_filename)
        self.assertGreater(len(loaded_data), 0)


if __name__ == '__main__':
    unittest.main()
