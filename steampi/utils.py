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
