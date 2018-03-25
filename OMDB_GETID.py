# Install the Python Requests library:
# `pip install requests`

import requests


def send_request():
    # GET ID
    # GET http://www.omdbapi.com/

    try:
        response = requests.get(
            url="http://www.omdbapi.com/",
            params={
                "i": "tt3501632",
                "apikey": "4f05a448",
            },
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
send_request()