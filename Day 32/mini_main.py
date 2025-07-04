import smtplib
import datetime as dt
import random

EMAIL = "shankhasmtp@gmail.com"
PASSWORD = "abcd123()"

now = dt.datetime.now()
week_day = now.weekday()

if week_day == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  # to make the connection secure
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Friday Motivation\n\n{quote}"
        )