# noinspection PyPep8Naming
import Levenshtein as lv
import steamspypi


def compute_all_game_name_distances_with_levenshtein(input_game_name, steamspy_database=None):
    if steamspy_database is None:
        steamspy_database = steamspypi.load()

    lower_case_input = input_game_name.lower()

    text_distances = dict()

    for app_id in steamspy_database:
        text = steamspy_database[app_id]['name']

        # Compare names in lower cases, to avoid mismatches for Tekken vs. TEKKEN, or Warhammer vs. WARHAMMER
        text_distances[app_id] = lv.distance(lower_case_input, text.lower())

    return text_distances
