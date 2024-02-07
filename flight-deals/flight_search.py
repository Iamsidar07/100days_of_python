import os

import requests

from flight_data import FlightData

KIWI_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
FLIGHT_SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
apikey = os.environ.get("FLIGHT_SEARCH_API_KEY")
headers = {
    "apikey": apikey,
}


class FlightSearch:
    def get_destination_code(self, city_name):
        params = {"term": city_name, "location_types": "city"}
        response = requests.get(url=KIWI_ENDPOINT, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data["locations"][0]["code"]

    def check_flights(
        self,
        origin_city_iata,
        destination_iata,
        date_from,
        date_to,
        min_staying_day=7,
        max_staying_day=28,
        currency="USD",
    ):
        query = {
            "fly_from": origin_city_iata,
            "fly_to": destination_iata,
            "date_from": date_from.strftime("%d/%m/%Y"),
            "date_to": date_to.strftime("%d/%m/%Y"),
            "nights_in_dst_from": min_staying_day,
            "nights_in_dst_to": max_staying_day,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stepover": 0,
            "curr": currency,
        }
        response = requests.get(
            url=FLIGHT_SEARCH_ENDPOINT, params=query, headers=headers
        )
        response.raise_for_status()
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_iata}")
            query["max_stepover"] = 1
            response = requests.get(
                url=FLIGHT_SEARCH_ENDPOINT, params=query, headers=headers
            )
            response.raise_for_status()
            data = response.json()["data"][0]
            flight_data = FlightData(
                price=data["price"],
                destination_airport=data["route"][0]["flyTo"],
                destination_city=data["route"][0]["cityTo"],
                origin_airport=data["route"][0]["flyFrom"],
                origin_city=data["route"][0]["cityFrom"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][0]["local_arrival"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"],
            )
            return flight_data
        flight_data = FlightData(
            price=data["price"],
            destination_airport=data["route"][0]["flyTo"],
            destination_city=data["route"][0]["cityTo"],
            origin_airport=data["route"][0]["flyFrom"],
            origin_city=data["route"][0]["cityFrom"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][0]["local_arrival"].split("T")[0],
        )
        print(f"{flight_data.destination_city}: ${flight_data.price}")
        return flight_data
