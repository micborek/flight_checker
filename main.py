import requests
import json
import time
import os
import logging

logging.basicConfig(level=logging.INFO,  # Set the logging level
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Set your client ID and client secret - move somewhere safe
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

# OpenSky token URL
token_url = "https://auth.opensky-network.org/auth/realms/opensky-network/protocol/openid-connect/token"
# Prepare payload for the request to get the access token
payload = {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET
}
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
response = requests.post(token_url, headers=headers, data=payload)

# Check if the request was successful
if response.status_code == 200:
    # Extract the access token from the response JSON
    access_token = response.json().get('access_token')
    logging.info("Access Token retrieved.")
else:
    logging.error("Failed to retrieve access token.")

# Now you can use the access token to make authorized requests to the OpenSky API
api_headers = {
    'Authorization': f'Bearer {access_token}'
}

longitude_min = '19.05233822999374' # W
longitude_max = '19.146976137518795' # E
latitude_min = '50.33709634597293' # N
latitude_max = '50.2816718464173' # S
time_secs = 3540

# Get the current time in seconds since epoch
current_time = time.time()

# Subtract one hour (3600 seconds)
one_hour_ago = current_time - 3600

print("One hour ago (epoch time):", one_hour_ago)

data = requests.get(f'https://opensky-network.org/api/states/all?time={int(one_hour_ago)}&lamin={latitude_min}&lomin={longitude_min}&lamax={latitude_max}&lomax={longitude_max}',  headers=api_headers)
flights_data =  json.loads(data.text).get('states')
print(flights_data)
