# SteamPI: a simple API for Steam

[![PyPI status][PyPI image]][PyPI] [![Build status][Build image]][Build] [![Updates][Dependency image]][PyUp] [![Python 3][Python3 image]][PyUp] [![Code coverage][Coveralls image]][Coveralls] [![Code coverage BIS][Codecov image]][Codecov]

  [PyPI]: https://pypi.python.org/pypi/steampi
  [PyPI image]: https://badge.fury.io/py/steampi.svg

  [Build]: https://travis-ci.org/woctezuma/steampi
  [Build image]: https://travis-ci.org/woctezuma/steampi.svg?branch=master

  [PyUp]: https://pyup.io/repos/github/woctezuma/steampi/
  [Dependency image]: https://pyup.io/repos/github/woctezuma/steampi/shield.svg
  [Python3 image]: https://pyup.io/repos/github/woctezuma/steampi/python-3-shield.svg

  [Coveralls]: https://coveralls.io/github/woctezuma/steampi?branch=master
  [Coveralls image]: https://coveralls.io/repos/github/woctezuma/steampi/badge.svg?branch=master

  [Codecov]: https://codecov.io/gh/woctezuma/steampi
  [Codecov image]: https://codecov.io/gh/woctezuma/steampi/branch/master/graph/badge.svg

This repository contains Python code to download some data through Steam API.

## Installation

The code is packaged for [PyPI](https://pypi.org/project/steampi/), so that the installation consists in running:

```bash
pip install steampi
```

## Usage

### Find the most similar game names to an input text

```python
import steamspypi
import steampi.calendar

steamspy_database = steamspypi.load()

input_text = 'Crash Bandicoot'
sorted_app_ids, text_distances = steampi.text_distances.find_most_similar_game_names(input_text, steamspy_database)

num_games_to_print = 5
for i in range(num_games_to_print):
    similar_game_name = steamspy_database[sorted_app_ids[i]] 
    print(similar_game_name)
```

### Retrieve the release year of a Steam game, given its appID

```python
import steampi.calendar

app_id = '440'
release_year = steampi.calendar.get_release_year(app_id)
```

### Retrieve the release date of a Steam game, given its appID

```python
import steampi.calendar

app_id = '440'
release_date = steampi.calendar.get_release_date_as_datetime(app_id)
```

### Download app details for of a Steam game, given its appID

```python
import steampi.api

app_id = '440'
(app_details, is_success, status_code) = steampi.api.load_app_details(app_id)
```
