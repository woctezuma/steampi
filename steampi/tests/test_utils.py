import string
import unittest

import steampi


class TestUtilsMethods(unittest.TestCase):
    def test_build_lower_case_game_name_dictionary(self):
        lower_case_game_name_dictionary = steampi.build_lower_case_game_name_dictionary()

        self.assertGreater(len(lower_case_game_name_dictionary), 0)

    def test_remove_characters_from_str(self):
        input_str = 'Hello, World!'
        characters_to_remove = string.punctuation

        edited_str = steampi.remove_characters_from_str(input_str=input_str,
                                                              characters_to_remove=characters_to_remove)

        self.assertEqual(edited_str, 'Hello World')


if __name__ == '__main__':
    unittest.main()
