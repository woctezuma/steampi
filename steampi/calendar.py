import datetime

import steampi.api


def get_release_date_as_str(app_id):
    app_details, _, _ = steampi.api.load_app_details(app_id)

    try:
        release_date = app_details[app_id]['data']['release_date']['date']
    except KeyError:
        try:
            release_date = app_details['release_date']['date']
        except KeyError:
            release_date = None

    return release_date


def get_release_date_as_datetime(app_id):
    release_date_as_str = get_release_date_as_str(app_id)

    if release_date_as_str is not None and release_date_as_str == '':
        release_date = None
    else:

        try:
            # Reference: https://stackoverflow.com/a/6557568/
            release_date = datetime.datetime.strptime(release_date_as_str, '%d %b, %Y')
        except ValueError:
            release_date = datetime.datetime.strptime(release_date_as_str, '%b %d, %Y')
        except TypeError:
            release_date = None

    return release_date


def get_release_year(app_id):
    release_date = get_release_date_as_datetime(app_id)

    if release_date is not None:
        release_year = release_date.year
    else:
        release_year = -1

    return release_year
