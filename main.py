import requests
import json
import logging
from helpers import get_access_token, get_time_epoch
from constants import LATITUDE_MAX, LONGITUDE_MAX, LATITUDE_MIN, LONGITUDE_MIN, TIME_SECS

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

access_token = get_access_token()
if access_token:
    logging.info("Access Token retrieved.")
else:
    logging.error("Failed to retrieve access token")

# Now you can use the access token to make authorized requests to the OpenSky API
api_headers = {
    'Authorization': f'Bearer {access_token}'
}

data = requests.get(
    f'https://opensky-network.org/api/states/all?time={int(get_time_epoch())}&lamin={LATITUDE_MIN}&lomin={LONGITUDE_MIN}&lamax={LATITUDE_MAX}&lomax={LONGITUDE_MAX}',
    headers=api_headers)
flights_data = json.loads(data.text).get('states')

if not flights_data:
    logging.info('No flights found for a previous hour in the area.')
else:
    for flight in flights_data:
        logging.info(f'Flight found - {flight}')