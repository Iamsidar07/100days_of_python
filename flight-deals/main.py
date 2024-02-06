from datetime import datetime, timedelta

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "LON"

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
for city in sheet_data:
    if len(city["iataCode"]) == 0:
        flight_search = FlightSearch()
        city["iataCode"] = flight_search.get_destination_code(city_name=city["city"])
data_manager.destination_data = sheet_data
data_manager.update_destination_data()

tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=6 * 30)

for destination in sheet_data:
    flight_search = FlightSearch()
    flights = flight_search.check_flights(
        origin_city_iata=ORIGIN_CITY_IATA,
        destination_iata=destination["iataCode"],
        min_staying_day=7,
        max_staying_day=28,
        date_from=tomorrow,
        date_to=six_months_from_today,
        currency="GBP",
    )
    if len(flights) != 0:
        for flight in flights:
            price = flight["price"]
            if price <= destination["lowestPrice"]:
                # send msg
                notification = NotificationManager()
                notification.send_msg(
                    message=f"""Low price alert! Only for ${flight['price']} to fly from 
                    {flight['cityFrom']}-{flight['flyFrom']} to {flight['cityTo']}-{flight['flyTo']}."""
                )
