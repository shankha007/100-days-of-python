import smtplib
import datetime as dt
import pandas
import random

EMAIL = "shankhasmtp@gmail.com"
PASSWORD = "abcd1234()"

birthday_df = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in birthday_df.iterrows()}
today = (dt.datetime.now().month, dt.datetime.now().day)


if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday {birthday_person["name"]}!\n\n{contents}"
        )