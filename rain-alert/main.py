import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

URL = "https://api.openweathermap.org/data/2.5/forecast"
MY_LAT = 23.116240
MY_LONG = 83.195923
API_KEY = os.getenv("API_KEY")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_ = os.getenv("FROM_")
to = os.getenv("TO")
client = Client(account_sid, auth_token)
parameters = {
    "lat": MY_LAT, 
    "lon": MY_LONG, 
    "cnt": 4, 
    "appid": API_KEY
    }

response = requests.get(url=URL, params=parameters)
response.raise_for_status()
data = response.json()
will_rain = False
for weather in data["list"]:
    weather_id = int(weather["weather"][0]["id"])
    if weather_id < 700:
        print("bring umbrella")
        will_rain = True

if will_rain:
    # Send text sms0
    message = client.messages.create(
        from_=from_,
        to=to,
        body="Take umbrella☂️ with you. It's rainny today!",
    )
    print(message)
