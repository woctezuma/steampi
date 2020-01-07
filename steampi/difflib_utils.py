import difflib
import heapq

from steampi.utils import build_lower_case_game_name_dictionary


def compute_all_game_name_distances_with_diff_lib(input_game_name,
                                                  steamspy_database=None,
                                                  n=3,
                                                  junk_str='',
                                                  cutoff=0.6,
                                                  ):
    lower_case_input = input_game_name.lower()

    lower_case_game_name_dictionary = build_lower_case_game_name_dictionary(steamspy_database)

    lower_case_references = lower_case_game_name_dictionary.keys()

    close_matches_and_similarity_ratios = get_close_matches_and_similarity_ratios(word=lower_case_input,
                                                                                  possibilities=lower_case_references,
                                                                                  n=n,
                                                                                  junk_str=junk_str,
                                                                                  cutoff=cutoff)

    text_distances = dict()

    for (lower_case_text, similarity_ratio) in close_matches_and_similarity_ratios:
        app_id = lower_case_game_name_dictionary[lower_case_text]

        # Reference: https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.ratio
        textual_distance = 1 - similarity_ratio

        text_distances[app_id] = textual_distance

    return text_distances


def get_close_matches_and_similarity_ratios(word, possibilities, n=3, cutoff=0.6, junk_str=''):
    """Use SequenceMatcher to return list of the best "good enough" matches, along with the similarity ratios.

    Code inspired from:
        https://docs.python.org/3/library/difflib.html#difflib.get_close_matches

    word is a sequence for which close matches are desired (typically a
    string).

    possibilities is a list of sequences against which to match word
    (typically a list of strings).

    Optional arg n (default 3) is the maximum number of close matches to
    return.  n must be > 0.

    Optional arg cutoff (default 0.6) is a float in [0, 1].  Possibilities
    that don't score at least that similar to word are ignored.

    Optional arg junk_str (default '') is a string containing all the junk
    characters, which are to be omitted.

    The best (no more than n) matches among the possibilities are returned
    in a list, sorted by similarity score, most similar first.

    >>> get_close_matches_and_similarity_ratios("appel", ["ape", "apple", "peach", "puppy"])
    [('apple', 0.8), ('ape', 0.75)]
    >>> import keyword as _keyword
    >>> get_close_matches_and_similarity_ratios("wheel", _keyword.kwlist)
    [('while', 0.6)]
    >>> get_close_matches_and_similarity_ratios("Apple", _keyword.kwlist)
    []
    >>> get_close_matches_and_similarity_ratios("accept", _keyword.kwlist)
    [('except', 0.6666666666666666)]
    """

    if not n > 0:
        raise ValueError("n must be > 0: %r" % (n,))
    if not 0.0 <= cutoff <= 1.0:
        raise ValueError("cutoff must be in [0.0, 1.0]: %r" % (cutoff,))
    result = []
    if len(junk_str) > 0:
        s = difflib.SequenceMatcher(isjunk=lambda x: x in junk_str)
    else:
        s = difflib.SequenceMatcher()
    s.set_seq2(word)
    for x in possibilities:
        s.set_seq1(x)
        if s.real_quick_ratio() >= cutoff and \
                s.quick_ratio() >= cutoff and \
                s.ratio() >= cutoff:
            result.append((s.ratio(), x))

    # Move the best scorers to head of list
    result = heapq.nlargest(n, result)
    # Swap scorers and scores for the best n matches
    close_matches_and_similarity_ratios = [(x, score) for score, x in result]

    return close_matches_and_similarity_ratios
