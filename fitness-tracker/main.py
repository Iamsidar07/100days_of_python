import requests
from datetime import datetime
import os

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
GOOGLE_SHEET_TOKEN = os.environ.get("GOOGLE_SHEET_TOKEN")
GOOGLE_SHEETY_ENDPOINT = os.environ.get("GOOGLE_SHEETY_ENDPOINT")

NUTRITIONIX_BASE_URL = "https://trackapi.nutritionix.com"
NUTRITIONIX_ENDPOINT = "/v2/natural/exercise"


headers = {
    "Content-Type": "application/json", 
    "x-app-id": APP_ID, 
    "x-app-key": API_KEY
}

request_body = {
    "query": input("Tell me what exercies you did: ")
}

response = requests.post(
    url=f"{NUTRITIONIX_BASE_URL}{NUTRITIONIX_ENDPOINT}",
    json=request_body,
    headers=headers,
)
response.raise_for_status()
data = response.json()["exercises"]

now = datetime.now().strftime("%d/%m/%Y")
current_time = datetime.now().strftime("%H:%M:%S")

google_sheety_headers = {
    "Authorization": f"Bearer {GOOGLE_SHEET_TOKEN}"
}

for exercies_data in data:
    exercise = exercies_data["name"]
    duration = exercies_data["duration_min"]
    calories = exercies_data["nf_calories"]
    google_sheety_req_body = {
        "workout": {
            "date": now,
            "time": current_time,
            "exercise": exercise.title(),
            "duration": duration,
            "calories": calories,
        }
    }
    response = requests.post(
        url=GOOGLE_SHEETY_ENDPOINT,
        json=google_sheety_req_body,
        headers=google_sheety_headers,
    )
    response.raise_for_status()
    exercies_data = response.json()
    print(exercies_data["workout"])