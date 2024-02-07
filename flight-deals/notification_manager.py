import os

from twilio.rest import Client
from smtplib import SMTP

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
from_ = os.environ.get("FROM_")
to = os.environ.get("TO")
my_email = os.getenv("MY_EMAIL")
password = os.getenv("PASSWORD")


class NotificationManager:
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_msg(self, message):
        msg = self.client.messages.create(from_=from_, to=to, body=message)
        print(msg.status)

    def send_email(self, emails, message):
        with SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            for email in emails:
                connection.sendmail(
                    from_addr=my_email,
                    msg=f"Subject:New Low price Flight!\n\n{message}".encode("utf-8"),
                    to_addrs=email
                )
