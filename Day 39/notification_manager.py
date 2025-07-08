import os
import env
from twilio.rest import Client


class NotificationManager:

    def __init__(self):
        self.client = Client(env.TWILIO_ACCOUNT_SID, env.TWILIO_AUTH_TOKEN)

    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:{os.environ["TWILIO_WHATSAPP_NUMBER"]}',
            body=message_body,
            to=f'whatsapp:{os.environ["TWILIO_VERIFIED_NUMBER"]}'
        )
        print(message.sid)
