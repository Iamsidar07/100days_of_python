from smtplib import SMTP
import random

EMAIL = ""
To_EMAIL = random.choice([""])
PASSWORD = ""
messages = ['']


class EmailBot:
    def __init__(self) -> None:
        with SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr="prayas1430@gmail.com",
                to_addrs=To_EMAIL,
                msg=f"Subject:I love you!\n\n{random.choice(messages)}",
            )
            print("Sent email")
