import smtplib
import datetime as dt
import random

MY_EMAIL = "ms8460149@gmail.com"
PASSWORD = ""
TO_ADDR = "ms8460149@gmail.com"
SUBJECT = "Happy Birthday Wish"
MESSAGE = "Hello,\nWe wish you a very happy birthday to you.\nCheers,\nManoj Kumar"

# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.sendmail(
#     from_addr=FROM_ADDR,
#     to_addrs=TO_ADDR,
#     msg="Subject:Happy Birthday Wish\n\nHello,\nWe wish you a very happy birthday to you.\nCheers,\nManoj Kumar",
# )
# connection.close()


def send_email(to_addrs, subject="", msg=""):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=to_addrs,
            msg=f"Subject:{subject}\n\n{msg}",
        )


now = dt.datetime.now()
# day = now.day
# week_day = now.weekday()
# year = now.year
# month = now.month
# print(day,now, week_day, year, month)

birthday = dt.datetime(year=2024, month=1, day=30)

print(birthday.date() == now.date())

# with open("./quotes.txt") as file:
#     quotes = file.readlines()
#     random_quote = random.choice(quotes)

# now = dt.datetime.now()
# weekday = now.weekday()
# print(random_quote)
# if weekday == 1:
#     # send email
#     send_email(to_addrs="monikasidar0@gmail.com", subject=SUBJECT, msg=MESSAGE)

