import requests
import datetime as dt
import smtplib
import time

MY_LAT = 23.116240
MY_LONG = 83.195923
MY_EMAIL = ""
PASSWORD = ""


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    print("is_iss_overhead: ", data)
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])
    return abs(MY_LAT - latitude) <= 5 and abs(MY_LONG - longitude) <= 5


def is_currently_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    print({sunrise, sunset})
    now = dt.datetime.now().hour
    return now < sunrise or now > sunset


while True:
    time.sleep(60)
    # is_iss_overhead and is_currently_dark send and email
    if is_iss_overhead() and is_currently_dark():
        # send email
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:Look up☝\n\nHey Manoj let's catch up the ISS now!"
            )
