# import smtplib
#
# my_email = "shankhasmtp@gmail.com"
# password = "abcd123()"
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls() # to make the connection secure
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="shankhasmtp@yahoo.com",
#         msg="Subject:Hello\n\nThis is the body of my email"
#     )

import datetime as dt

now = dt.datetime.now()
year = now.year
# print(type(now)) # <class 'datetime.datetime'>
# print(type(now.year)) # <class 'int'>
if year == 2025:
    print("It's 2025")
day_of_week = now.weekday()
print(day_of_week) # 4 (Friday)

date_of_birth = dt.datetime(year=1998, month=6, day=18)
print(date_of_birth) # 1998-06-18 00:00:00