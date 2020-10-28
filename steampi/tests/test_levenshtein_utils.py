import unittest

import steampi


class TestLevenshteinUtilsMethods(unittest.TestCase):

    def test_compute_all_game_name_distances_with_diff_lib(self):
        input_text = 'Crash Bandicoot'
        text_distances = steampi.compute_all_game_name_distances_with_levenshtein(input_text)

        self.assertGreater(len(text_distances), 0)


if __name__ == '__main__':
    unittest.main()
