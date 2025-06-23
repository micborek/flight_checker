import os

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

OPENSKY_TOKEN_URL = "https://auth.opensky-network.org/auth/realms/opensky-network/protocol/openid-connect/token"
LONGITUDE_MIN = '19.05233822999374'  # W
LONGITUDE_MAX = '19.146976137518795'  # E
LATITUDE_MIN = '50.33709634597293'  # N
LATITUDE_MAX = '50.2816718464173'  # S
TIME_SECS = 3600