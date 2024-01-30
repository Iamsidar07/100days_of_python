# deploy to pythonanywhere cloud
import pandas as pd
import datetime as dt
import random
import smtplib
import time

MY_EMAIL = "ms8460149@gmail.com"
PASSWORD = "lmfbnmkslbohnnjq"
SUBJECT = "Happy Birthday Wish"

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
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:{SUBJECT}\n\n{msg}",
        )
        print(f"Email sent to {birthday_person['name']}, email: {birthday_person['email']}")
    # wait for 500ms
    time.sleep(0.05)
