import difflib

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


def compute_all_game_name_distances_with_diff_lib(input_game_name,
                                                  steamspy_database=None,
                                                  reference_texts=None,
                                                  computation_type=None):
    if steamspy_database is None:
        steamspy_database = steamspypi.load()

    lower_case_game_name_dictionary = build_lower_case_game_name_dictionary(steamspy_database)

    if reference_texts is None:
        reference_texts = list(lower_case_game_name_dictionary.keys())

        lower_case_reference_texts = reference_texts
    else:
        lower_case_reference_texts = [text.lower() for text in reference_texts]

    if computation_type is None:
        computation_type = 'exact'

    lower_case_input = input_game_name.lower()

    text_distances = dict()

    for lower_case_text in lower_case_reference_texts:
        app_id = lower_case_game_name_dictionary[lower_case_text]

        s = difflib.SequenceMatcher(None, lower_case_input, lower_case_text)

        # Reference: https://docs.python.org/3.8/library/difflib.html#difflib.SequenceMatcher.ratio
        if computation_type == 'exact':
            textual_similarity_ratio = s.ratio()
        elif computation_type == 'quick':
            textual_similarity_ratio = s.quick_ratio()
        else:
            textual_similarity_ratio = s.real_quick_ratio()

        textual_distance = 1 - textual_similarity_ratio

        text_distances[app_id] = textual_distance

    return text_distances


def find_most_similar_game_names_with_diff_lib(input_game_name,
                                               steamspy_database=None,
                                               computation_type=None,
                                               trim_possibilities=None,
                                               n=None,
                                               cutoff=None):
    if computation_type is None:
        # Either 'exact', 'quick', or 'real_quick'.
        computation_type = 'exact'

    if trim_possibilities is None:
        # Caveat: do not solely rely on "quick" or "real_quick" ratios! If you don't want to use the slow 'exact' ratio,
        #         then you will get more reliable results if you first trim the possibilities with get_close_matches()!
        trim_possibilities = bool(computation_type != 'exact')

    if n is None:
        # Only relevant if computation type is not equal to 'exact'
        n = 5

    if cutoff is None:
        # Only relevant if computation type is not equal to 'exact'
        cutoff = 0.6

    lower_case_input = input_game_name.lower()
    lower_case_game_name_dictionary = build_lower_case_game_name_dictionary(steamspy_database)

    if trim_possibilities:
        # Reference: https://docs.python.org/3.8/library/difflib.html#difflib.get_close_matches
        sorted_texts = difflib.get_close_matches(word=lower_case_input,
                                                 possibilities=lower_case_game_name_dictionary.keys(),
                                                 n=n,
                                                 cutoff=cutoff)
    else:
        sorted_texts = list(lower_case_game_name_dictionary.keys())

    text_distances = compute_all_game_name_distances_with_diff_lib(input_game_name,
                                                                   steamspy_database=steamspy_database,
                                                                   reference_texts=sorted_texts,
                                                                   computation_type=computation_type)

    sorted_app_ids = sorted(text_distances.keys(), key=lambda app_id: text_distances[app_id])

    return sorted_app_ids, text_distances
