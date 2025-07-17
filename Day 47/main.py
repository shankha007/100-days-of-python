from bs4 import BeautifulSoup
import requests
import smtplib

import env

# AMAZON_URL = "https://appbrewery.github.io/instant_pot/"

# AMAZON_URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
# SYMBOL = "$"

AMAZON_URL = "https://www.amazon.in/PlayStation%C2%AE5-Console-STD-SLIM-Bundle/dp/B0FG835ZCY/ref=sr_1_1"
SYMBOL = "₹"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0"
}

response = requests.get(url=AMAZON_URL, headers=headers)
html_doc = response.text

soup = BeautifulSoup(html_doc, 'html.parser')
price = soup.find(class_="a-offscreen").get_text()
# print(price)
price_without_currency = price.split(SYMBOL)[1]
# print(price_without_currency)
price_as_float = float(price_without_currency.replace(",", ""))
# print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
# print(title)

# Set the price below which you would like to get a notification
BUY_PRICE = 55000

if price_as_float < BUY_PRICE:
    message = f"{title} is on sale for {price}!"
    with smtplib.SMTP(env.SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(env.FROM_EMAIL, env.PASSWORD)
        connection.sendmail(
            from_addr=env.FROM_EMAIL,
            to_addrs=env.TO_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{AMAZON_URL}".encode("utf-8")
        )
