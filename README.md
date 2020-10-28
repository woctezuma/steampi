# SteamPI: a simple API for Steam

[![PyPI status][pypi-image]][pypi]
[![Build status][build-image]][build]
[![Updates][dependency-image]][pyup]
[![Python 3][python3-image]][pyup]
[![Code coverage][codecov-image]][codecov]
[![Code Quality][codacy-image]][codacy]

This repository contains Python code to download some data through Steam API.

## Installation

The code is packaged for [PyPI](https://pypi.org/project/steampi/), so that the installation consists in running:

```bash
pip install steampi
```

## Usage

### Download app details of a Steam game, given its appID

```python
import steampi.api

app_id = '440'
(app_details, is_success, status_code) = steampi.api.load_app_details(app_id)
```

### Retrieve the release date of a Steam game, given its appID

```python
import steampi.calendar

app_id = '440'
release_date = steampi.calendar.get_release_date_as_datetime(app_id)
```

### Retrieve the release year of a Steam game, given its appID

```python
import steampi.calendar

app_id = '440'
release_year = steampi.calendar.get_release_year(app_id)
```

### Find the most similar game names to an input text

#### Using the Levenshtein distance

The Levenshtein distance is an edit distance, which is useful to fix typos for instance.

```python
import steampi.text_distances
import steamspypi

steamspy_database = steamspypi.load()

input_text = 'Crash Bandicoot'
sorted_app_ids, text_distances = steampi.text_distances.find_most_similar_game_names(input_text,
                                                                                     steamspy_database)

num_games_to_print = 5
for i in range(num_games_to_print):
    similar_game_name = steamspy_database[sorted_app_ids[i]]
    print(similar_game_name)
```

#### Using the longest contiguous matching subsequence

The code snippet below makes use of the longest contiguous matching subsequence.
This leads to different results compared to Levenshtein distance, which you might find more suitable for your needs.

However:
-   the code is slower than with Levenshtein distance: for instance, the run-time is 140% longer for the unit test,
-   the text distances are bound to [0,1], so they do not have the same value range as for Levenshtein distance,
-   the text distances do not have the same meaning as for Levenshtein distance, which was the minimal number of edits,
-   the results do not contain all the text distances, but only these with less than 0.4 distance (i.e. 0.6 similarity).

Junk characters can be specified with `junk_str`.

```python
import steampi.text_distances
import steamspypi

steamspy_database = steamspypi.load()

num_games_to_print = 5
junk_str=''

input_text = 'Crash Bandicoot'
sorted_app_ids, text_distances = steampi.text_distances.find_most_similar_game_names(input_text,
                                                                                     steamspy_database,
                                                                                     use_levenshtein_distance=False,
                                                                                     n=num_games_to_print,
                                                                                     junk_str=junk_str,
                                                                                     )

for i in range(len(sorted_app_ids)):
    similar_game_name = steamspy_database[sorted_app_ids[i]]
    print(similar_game_name)
```

## References

-   [Levenshtein module](https://github.com/ztane/python-Levenshtein) for the Levenshtein distance,
-   [Difflib module](https://docs.python.org/3/library/difflib.html) for the longest contiguous matching subsequence.

<!-- Definitions for badges -->

[pypi]: <https://pypi.python.org/pypi/steampi>
[pypi-image]: <https://badge.fury.io/py/steampi.svg>

[build]: <https://github.com/woctezuma/steampi/actions>
[build-image]: <https://github.com/woctezuma/steampi/workflows/Python package/badge.svg?branch=master>
[publish-image]: <https://github.com/woctezuma/steampi/workflows/Upload Python Package/badge.svg?branch=master>

[pyup]: <https://pyup.io/repos/github/woctezuma/steampi/>
[dependency-image]: <https://pyup.io/repos/github/woctezuma/steampi/shield.svg>
[python3-image]: <https://pyup.io/repos/github/woctezuma/steampi/python-3-shield.svg>

[codecov]: <https://codecov.io/gh/woctezuma/steampi>
[codecov-image]: <https://codecov.io/gh/woctezuma/steampi/branch/master/graph/badge.svg>

[codacy]: <https://www.codacy.com/app/woctezuma/steampi>
[codacy-image]: <https://api.codacy.com/project/badge/Grade/b7c2295b2f69449dad7b553b2295c844>
