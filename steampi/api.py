import pathlib

import steampi.json_utils


def get_appdetails_url(app_id):
    url = 'https://store.steampowered.com/api/appdetails?appids=' + str(app_id)
    return url


def download_app_details(app_id):
    url = get_appdetails_url(app_id)
    (data, status_code) = steampi.json_utils.download_json_data(url)
    success_flag = bool(data is not None)

    downloaded_app_details = {}

    if success_flag:
        try:
            downloaded_app_details = data[app_id]['data']
        except KeyError:
            print('No data found for appID = {} with status code = {}'.format(app_id, status_code))

        try:
            success_flag = data[app_id]['success']
        except KeyError:
            success_flag = False

    return downloaded_app_details, success_flag, status_code


def get_appdetails_filename(app_id):
    # Objective: return the filename where app details for input appID are stored.

    data_path = steampi.json_utils.get_data_path() + "appdetails/"

    pathlib.Path(data_path).mkdir(parents=True, exist_ok=True)

    json_base_filename = "appID_" + str(app_id) + ".json"

    data_filename = data_path + json_base_filename

    return data_filename


def load_app_details(app_id):
    json_filename = get_appdetails_filename(app_id)

    try:
        loaded_app_details = steampi.json_utils.load_json_data(json_filename)
        success_flag = True
        status_code = None
    except FileNotFoundError:
        (loaded_app_details, success_flag, status_code) = download_app_details(app_id)
        if success_flag:
            steampi.json_utils.save_json_data(json_filename, loaded_app_details)

    return loaded_app_details, success_flag, status_code
