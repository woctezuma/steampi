import string

import steamspypi


def build_lower_case_game_name_dictionary(steamspy_database=None):
    # Build a Python dictionary mapping **lower-case** game names found in SteamSpy database to their Steam appID.

    if steamspy_database is None:
        steamspy_database = steamspypi.load()

    lower_case_game_name_dictionary = dict()

    for app_id in steamspy_database:
        text = steamspy_database[app_id]['name']

        lower_case_text = text.lower()

        lower_case_game_name_dictionary[lower_case_text] = app_id

    return lower_case_game_name_dictionary


def remove_characters_from_str(input_str, characters_to_remove=None):
    # Reference: https://stackoverflow.com/a/266162

    if characters_to_remove is None:
        characters_to_remove = string.punctuation

    edited_str = input_str.translate(str.maketrans('', '', characters_to_remove))

    return edited_str
