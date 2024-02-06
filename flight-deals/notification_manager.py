import os

from twilio.rest import Client

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
from_ = os.environ.get("FROM_")
to = os.environ.get("TO")


class NotificationManager:
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_msg(self, message):
        msg = self.client.messages.create(from_=from_, to=to, body=message)
        print(msg.status)
