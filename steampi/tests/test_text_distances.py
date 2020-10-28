import unittest

import steamspypi

import steampi


class TestTextDistancesMethods(unittest.TestCase):
    def test_compute_all_game_name_distances(self):
        input_text = 'Crash Bandicoot'
        text_distances = steampi.compute_all_game_name_distances(input_text)

        self.assertGreater(len(text_distances), 0)

    def test_find_most_similar_game_names_with_levenshtein(self):
        steamspy_database = steamspypi.load()

        input_text = 'Crash Bandicoot'
        sorted_app_ids, text_distances = steampi.find_most_similar_game_names(input_text,
                                                                                             steamspy_database,
                                                                                             use_levenshtein_distance=True,
                                                                                             )

        num_games_to_print = 10

        print('Using the Levenshtein distance for input {}:'.format(input_text))
        for i in range(num_games_to_print):
            app_id = sorted_app_ids[i]
            similar_game = steamspy_database[app_id]
            textual_distance = text_distances[app_id]

            similar_game_name = similar_game['name']

            print('{}) distance = {} ; {}'.format(i + 1,
                                                  textual_distance,
                                                  similar_game_name))

        self.assertGreater(len(sorted_app_ids), 0)

    def test_find_most_similar_game_names_with_diff_lib(self):
        steamspy_database = steamspypi.load()

        num_games_to_print = 10

        input_text = 'Crash Bandicoot'
        sorted_app_ids, text_distances = steampi.find_most_similar_game_names(input_text,
                                                                                             steamspy_database,
                                                                                             use_levenshtein_distance=False,
                                                                                             n=num_games_to_print)

        print('Using the longest contiguous matching subsequence for input {}:'.format(input_text))
        for i in range(num_games_to_print):
            try:
                app_id = sorted_app_ids[i]
            except IndexError:
                continue

            similar_game = steamspy_database[app_id]
            textual_distance = text_distances[app_id]

            similar_game_name = similar_game['name']

            print('{}) distance = {} ; {}'.format(i + 1,
                                                  textual_distance,
                                                  similar_game_name))

        self.assertGreater(len(sorted_app_ids), 0)


if __name__ == '__main__':
    unittest.main()
