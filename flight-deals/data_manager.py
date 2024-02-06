import os

import requests

google_sheet_endpoint = os.environ.get("FLIGHT_DEALS_GOOGLE_SHEET_ENDPOINT")
google_sheet_token = os.environ.get("FLIGHT_DEALS_GOOGLE_SHEET_TOKEN")
headers = {"Authorization": f"Bearer {google_sheet_token}"}


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=google_sheet_endpoint, headers=headers)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_data(self):
        for city in self.destination_data:
            new_data = {"price": {"iataCode": city["iataCode"]}}
            response = requests.put(
                url=f"{google_sheet_endpoint}/{city['id']}",
                json=new_data,
                headers=headers,
            )
            response.raise_for_status()
            print(response.text)
