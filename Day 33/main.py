import requests
from datetime import datetime
import math
import time
import smtplib

MY_LAT = 18.520430
MY_LONG = 73.856743

EMAIL = "shankhasmtp@gmail.com"
PASSWORD = "abcd()"

#Your position is within +5 or -5 degrees of the ISS position.
def is_iss_overhead():
    res = requests.get(url="http://api.open-notify.org/iss-now.json")
    res.raise_for_status()
    dt = res.json()

    iss_latitude = float(dt["iss_position"]["latitude"])
    iss_longitude = float(dt["iss_position"]["longitude"])

    return math.fabs(MY_LAT - iss_latitude) <= 5 and math.fabs(MY_LONG - iss_longitude) <= 5

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    res = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    res.raise_for_status()
    data = res.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    return sunset <= time_now <= sunrise


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=EMAIL,
                msg=f"Subject:Look Up\n\nThe ISS is above you in the sky!!"
            )