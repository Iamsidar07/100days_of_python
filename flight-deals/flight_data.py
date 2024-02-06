import os

import requests

google_sheet_endpoint = os.environ.get("FLIGHT_DEALS_GOOGLE_SHEET_ENDPOINT")
google_sheet_token = os.environ.get("FLIGHT_DEALS_GOOGLE_SHEET_TOKEN")
headers = {"Authorization": f"Bearer {google_sheet_token}"}


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        response = requests.get(url=google_sheet_endpoint, headers=headers)
        response.raise_for_status()
        self.data = response.json()["prices"]
