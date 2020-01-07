from .difflib_utils import compute_all_game_name_distances_with_diff_lib
from .levenshtein_utils import compute_all_game_name_distances_with_levenshtein


def compute_all_game_name_distances(input_game_name,
                                    steamspy_database=None,
                                    use_levenshtein_distance=True,
                                    n=3,
                                    junk_str='',
                                    cutoff=0.6):
    if use_levenshtein_distance:
        # Levenshtein distance
        text_distances = compute_all_game_name_distances_with_levenshtein(input_game_name,
                                                                          steamspy_database)
    else:
        # The longest contiguous matching subsequence
        # Reference: https://docs.python.org/3/library/difflib.html
        text_distances = compute_all_game_name_distances_with_diff_lib(input_game_name,
                                                                       steamspy_database,
                                                                       n=n,
                                                                       junk_str=junk_str,
                                                                       cutoff=cutoff)

    return text_distances


def find_most_similar_game_names(input_game_name,
                                 steamspy_database=None,
                                 use_levenshtein_distance=True,
                                 n=3,
                                 junk_str='',
                                 cutoff=0.6):
    text_distances = compute_all_game_name_distances(input_game_name,
                                                     steamspy_database=steamspy_database,
                                                     use_levenshtein_distance=use_levenshtein_distance,
                                                     n=n,
                                                     junk_str=junk_str,
                                                     cutoff=cutoff,
                                                     )

    sorted_app_ids = sorted(text_distances.keys(), key=lambda app_id: text_distances[app_id])

    return sorted_app_ids, text_distances
