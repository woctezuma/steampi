import unittest

import steampi.utils


class TestUtilsMethods(unittest.TestCase):
    def test_build_lower_case_game_name_dictionary(self):
        lower_case_game_name_dictionary = steampi.utils.build_lower_case_game_name_dictionary()

        self.assertGreater(len(lower_case_game_name_dictionary), 0)


if __name__ == '__main__':
    unittest.main()
