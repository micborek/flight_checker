import requests
import time
from constants import OPENSKY_TOKEN_URL, CLIENT_ID, CLIENT_SECRET, TIME_SECS


def get_access_token() -> str:
    """Get access token for Opensky API"""

    access_token = ''

    # Prepare payload for the request to get the access token
    payload = {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    response = requests.post(OPENSKY_TOKEN_URL, headers=headers, data=payload)

    if response.status_code == 200:
        # Extract the access token from the response JSON
        access_token = response.json().get('access_token')

    return access_token

def get_time_epoch():
    """Get epoch time to pass in the API. Current time minus a preferred period"""

    current_time = time.time()
    one_hour_ago = current_time - TIME_SECS

    return int(one_hour_ago)
