import json

import requests


def get_data_path():
    return 'data/'


def download_json_data(url, verbose=True):
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
    else:
        data = None
        if verbose:
            print('Faulty response status code = {} for url = {}'.format(response.status_code, url))

    return data, response.status_code


def save_json_data(json_filename, json_data):
    json_as_str = json.dumps(json_data)

    with open(json_filename, 'w', encoding='utf8') as f:
        # Reference: https://stackoverflow.com/a/8710579/
        print(json_as_str, file=f)

    return True


def load_json_data(json_filename):
    with open(json_filename, 'r', encoding='utf8') as f:
        data = json.load(f)

    return data
