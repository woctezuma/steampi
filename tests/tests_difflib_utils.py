import unittest

import steamspypi

import steampi.difflib_utils


class TestDifflibUtilsMethods(unittest.TestCase):
    def test_build_lower_case_game_name_dictionary(self):
        steamspy_database = steamspypi.load()

        lower_case_game_name_dictionary = steampi.difflib_utils.build_lower_case_game_name_dictionary(steamspy_database)

        self.assertGreater(len(lower_case_game_name_dictionary), 0)

    def test_compute_all_game_name_distances_with_diff_lib(self):
        input_text = 'Crash Bandicoot'
        text_distances = steampi.difflib_utils.compute_all_game_name_distances_with_diff_lib(input_text,
                                                                                             computation_type='quick')

        self.assertGreater(len(text_distances), 0)

    def test_find_most_similar_game_names_with_diff_lib_real_quick_ratio(self):
        steamspy_database = steamspypi.load()

        num_games_to_print = 5

        input_text = 'Crash Bandicoot'
        sorted_app_ids, text_distances = steampi.difflib_utils.find_most_similar_game_names_with_diff_lib(input_text,
                                                                                                          steamspy_database,
                                                                                                          n=num_games_to_print,
                                                                                                          computation_type='real_quick',
                                                                                                          trim_possibilities=False)

        for i in range(num_games_to_print):
            try:
                app_id = sorted_app_ids[i]
            except IndexError:
                continue

            similar_game_name = steamspy_database[app_id]
            textual_distance = text_distances[app_id]

            print('{}) distance = {} ; {}'.format(i + 1,
                                                  textual_distance,
                                                  similar_game_name))

        self.assertGreater(len(sorted_app_ids), 0)

    def test_find_most_similar_game_names_with_diff_lib_quick_ratio(self):
        steamspy_database = steamspypi.load()

        num_games_to_print = 5

        input_text = 'Crash Bandicoot'
        sorted_app_ids, text_distances = steampi.difflib_utils.find_most_similar_game_names_with_diff_lib(input_text,
                                                                                                          steamspy_database,
                                                                                                          n=num_games_to_print,
                                                                                                          computation_type='quick',
                                                                                                          trim_possibilities=False)

        for i in range(num_games_to_print):
            try:
                app_id = sorted_app_ids[i]
            except IndexError:
                continue

            similar_game_name = steamspy_database[app_id]
            textual_distance = text_distances[app_id]

            print('{}) distance = {} ; {}'.format(i + 1,
                                                  textual_distance,
                                                  similar_game_name))

        self.assertGreater(len(sorted_app_ids), 0)

    def test_find_most_similar_game_names_with_diff_lib_exact_ratio(self):
        steamspy_database = steamspypi.load()

        input_text = 'Crash Bandicoot'
        sorted_app_ids, text_distances = steampi.difflib_utils.find_most_similar_game_names_with_diff_lib(input_text,
                                                                                                          steamspy_database,
                                                                                                          computation_type='exact',
                                                                                                          trim_possibilities=False)

        num_games_to_print = 5
        for i in range(num_games_to_print):
            app_id = sorted_app_ids[i]
            similar_game_name = steamspy_database[app_id]
            textual_distance = text_distances[app_id]

            print('{}) distance = {} ; {}'.format(i + 1,
                                                  textual_distance,
                                                  similar_game_name))

        self.assertGreater(len(sorted_app_ids), 0)


if __name__ == '__main__':
    unittest.main()
