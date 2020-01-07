# noinspection PyPep8Naming
import Levenshtein as lv
import steamspypi

from .difflib_utils import find_most_similar_game_names_with_diff_lib


def compute_all_game_name_distances(input_game_name, steamspy_database=None):
    if steamspy_database is None:
        steamspy_database = steamspypi.load()

    lower_case_input = input_game_name.lower()

    text_distances = dict()

    for app_id in steamspy_database:
        text = steamspy_database[app_id]['name']

        # Compare names in lower cases, to avoid mismatches for Tekken vs. TEKKEN, or Warhammer vs. WARHAMMER
        text_distances[app_id] = lv.distance(lower_case_input, text.lower())

    return text_distances


def find_most_similar_game_names_with_levenshtein_distance(input_game_name, steamspy_database=None):
    text_distances = compute_all_game_name_distances(input_game_name, steamspy_database)

    sorted_app_ids = sorted(text_distances.keys(), key=lambda app_id: text_distances[app_id])

    return sorted_app_ids, text_distances


def find_most_similar_game_names(input_game_name,
                                 steamspy_database=None,
                                 distance_type='lv',
                                 computation_type=None,
                                 trim_possibilities=None,
                                 n=None,
                                 cutoff=None):
    if distance_type in ['Levenshtein', 'lv']:

        sorted_app_ids, text_distances = find_most_similar_game_names_with_levenshtein_distance(
            input_game_name,
            steamspy_database,
        )

    else:

        sorted_app_ids, text_distances = find_most_similar_game_names_with_diff_lib(
            input_game_name,
            steamspy_database,
            computation_type=computation_type,
            trim_possibilities=trim_possibilities,
            n=n,
            cutoff=cutoff,
        )

    return sorted_app_ids, text_distances
