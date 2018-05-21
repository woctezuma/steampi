import unittest

import steamspypi

import steampi.text_distances


class TestTextDistancesMethods(unittest.TestCase):
    def test_compute_all_game_name_distances(self):
        input_game_name = 'Crash Bandicoot'
        text_distances = steampi.text_distances.compute_all_game_name_distances(input_game_name)
        self.assertGreater(len(text_distances), 0)

    def test_find_most_similar_game_names(self):
        input_game_name = 'Crash Bandicoot'
        steamspy_database = steamspypi.load()
        sorted_app_ids, _ = steampi.text_distances.find_most_similar_game_names(input_game_name, steamspy_database)
        for i in range(5):
            print(steamspy_database[sorted_app_ids[i]])
        self.assertGreater(len(sorted_app_ids), 0)


if __name__ == '__main__':
    unittest.main()
