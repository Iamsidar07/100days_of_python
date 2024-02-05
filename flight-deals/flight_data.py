import requests
GOOGLE_SHEET_ENDPOINT = "https://api.sheety.co/2d98cf2c677367f48c200f8bb7b0cbd1/flightDeals/prices"
GOOGLE_SHEET_TOKEN = "asdfjklowncaowljkamgoincoaieowjdkl"
headers = {
    "Authorization": f"Bearer {GOOGLE_SHEET_TOKEN}"
}

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        response = requests.get(url=GOOGLE_SHEET_ENDPOINT, headers=headers)
        response.raise_for_status()
        self.data = response.json()["prices"]
        