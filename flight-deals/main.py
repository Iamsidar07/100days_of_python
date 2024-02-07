from datetime import datetime, timedelta

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "LON"

data_manager = DataManager()
notification_manager = NotificationManager()
flight_search = FlightSearch()
sheet_data = data_manager.get_destination_data()
for city in sheet_data:
    if len(city["iataCode"]) == 0:
        city["iataCode"] = flight_search.get_destination_code(city_name=city["city"])
data_manager.destination_data = sheet_data
data_manager.update_destination_data()

tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=6 * 30)

for destination in sheet_data:
    flight = flight_search.check_flights(
        origin_city_iata=ORIGIN_CITY_IATA,
        destination_iata=destination["iataCode"],
        min_staying_day=7,
        max_staying_day=28,
        date_from=tomorrow,
        date_to=six_months_from_today,
        currency="GBP",
    )
    if flight is None:
        continue
    if flight.price <= destination["lowestPrice"]:
        users = data_manager.get_customers_emails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]
        message = f"Lowest price alert! Only for ${flight.price} from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}"
        if flight.stop_overs > 0:
            message += (
                f"Flight has {flight.stop_overs} stop overs, via {flight.via_city}."
            )
        notification_manager.send_msg(message=message)
        notification_manager.send_email(emails, message)
