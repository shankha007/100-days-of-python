import requests
from twilio.rest import Client
import env

API_KEY = env.API_KEY
LAT = env.LAT
LONG = env.LONG
OWM_ENDPOINT = env.OWM_ENDPOINT
FROM_NUMBER = env.FROM_NUMBER
TO_NUMBER = env.TO_NUMBER
account_sid = env.account_sid
auth_token = env.auth_token

parameters = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(OWM_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"]:
    if int(hour_data["weather"][0]["id"]) < 700:
        will_rain = True
        break

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔",
        from_=FROM_NUMBER,
        to=TO_NUMBER,
    )
    print(message.status)