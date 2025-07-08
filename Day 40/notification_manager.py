import smtplib
import env
from twilio.rest import Client


class NotificationManager:

    def __init__(self):
        self.smtp_address = env.EMAIL_PROVIDER_SMTP_ADDRESS
        self.email = env.MY_EMAIL
        self.email_password = env.MY_EMAIL_PASSWORD
        self.twilio_verified_number = env.TWILIO_TO_NUMBER
        self.whatsapp_number = env.TWILIO_FROM_NUMBER
        self.client = Client(env.TWILIO_ACCOUNT_SID, env.TWILIO_AUTH_TOKEN)
        self.connection = smtplib.SMTP(env.EMAIL_PROVIDER_SMTP_ADDRESS)
        self.client = Client(env.TWILIO_ACCOUNT_SID, env.TWILIO_AUTH_TOKEN)

    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:{self.whatsapp_number}',
            body=message_body,
            to=f'whatsapp:{self.twilio_verified_number}'
        )
        print(message.sid)

    def send_emails(self, email_list, email_body):
        with self.connection:
            self.connection.starttls()
            self.connection.login(self.email, self.email_password)
            for email in email_list:
                self.connection.sendmail(
                    from_addr=self.email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode('utf-8')
                )
