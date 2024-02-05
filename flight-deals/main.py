#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager
from notification_manager import NotificationManager

fligh_search = FlightSearch()
flight_data = FlightData()
data_manager = DataManager()
notification_manager = NotificationManager()

print(flight_data.data)
