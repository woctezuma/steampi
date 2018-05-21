import unittest

import steamspypi

import steampi.text_distances


class TestTextDistancesMethods(unittest.TestCase):
    def test_compute_all_game_name_distances(self):
        input_text = 'Crash Bandicoot'
        text_distances = steampi.text_distances.compute_all_game_name_distances(input_text)

        self.assertGreater(len(text_distances), 0)

    def test_find_most_similar_game_names(self):
        steamspy_database = steamspypi.load()

        input_text = 'Crash Bandicoot'
        sorted_app_ids, _ = steampi.text_distances.find_most_similar_game_names(input_text, steamspy_database)

        num_games_to_print = 5
        for i in range(num_games_to_print):
            similar_game_name = steamspy_database[sorted_app_ids[i]]
            print(similar_game_name)

        self.assertGreater(len(sorted_app_ids), 0)


if __name__ == '__main__':
    unittest.main()
