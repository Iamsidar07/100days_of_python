import pandas as pd
import datetime as dt
import random
import smtplib
import time
from dotenv import load_dotenv
import os

load_dotenv()


my_email = os.getenv("MY_EMAIL")
password = os.getenv("PASSWORD")
subject = "Happy Birthday Wish"

data = pd.read_csv("./data/birthdays.csv")
letter_path = ["./letters/letters_1.txt", "./letters/letters_2.txt"]
random_letter_path = random.choice(letter_path)

now = dt.datetime.now()
month = now.month
day = now.day


birthdays_list = data.to_dict(orient="records")

emails_to_send_today = [
    birthday
    for birthday in birthdays_list
    if day == birthday["day"] and birthday["month"] == month
]


for birthday_person in emails_to_send_today:
    # open letter
    with open(random_letter_path) as letter_file:
        letter = letter_file.read()
    # create msg
    msg = letter.strip().replace("[NAME]", birthday_person["name"])

    # send email with smtp
    
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:{subject}\n\n{msg}",
        )
        print(f"Email sent to {birthday_person['name']}, email: {birthday_person['email']}")
    # wait for 500ms
    time.sleep(0.05)
