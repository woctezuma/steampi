import unittest

import steampi


class TestDifflibUtilsMethods(unittest.TestCase):
    def test_build_lower_case_game_name_dictionary(self):
        lower_case_game_name_dictionary = (
            steampi.build_lower_case_game_name_dictionary()
        )

        assert len(lower_case_game_name_dictionary) > 0

    def test_compute_all_game_name_distances_with_diff_lib(self):
        input_text = 'Crash Bandicoot'
        cutoff = 0.5
        text_distances = steampi.compute_all_game_name_distances_with_diff_lib(
            input_text,
            cutoff=cutoff,
            verbose=True,
        )

        assert len(text_distances) > 0


if __name__ == '__main__':
    unittest.main()
