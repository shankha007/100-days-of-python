import env
import requests
import math
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": env.STOCK_API_KEY,
    "outputsize": "compact"
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()

daily_stock_price = stock_data["Time Series (Daily)"]
closing_stock_price = [(key, float(value["4. close"])) for (key, value) in daily_stock_price.items()]

diff_in_stock_price = math.fabs(closing_stock_price[0][1] - closing_stock_price[1][1])
percent_diff_in_stock_price = (diff_in_stock_price / closing_stock_price[0][1]) * 100

is_up = closing_stock_price[0][1] - closing_stock_price[1][1] > 0

if percent_diff_in_stock_price > 5:
    news_params = {
        "q": COMPANY_NAME,
        "from": closing_stock_price[0][0],
        "sortBy": "popularity",
        "apiKey": env.NEWS_API_KEY
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()
    top_3_articles = news_data["articles"][:3]
    print(top_3_articles)

    formatted_news = [{"headline": article["title"], "description": article["description"]} for article in top_3_articles]

    account_sid = env.TWILIO_ACCOUNT_SID
    auth_token = env.TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    for item in formatted_news:
        if is_up:
            up_or_down = "📈"
        else:
            up_or_down = "📉"

        content = f"{STOCK_NAME} {up_or_down} {int(percent_diff_in_stock_price)}%\n\nHeadline: {item["headline"]}\n\nBrief: {item["description"]}"

        # Trying Whatsapp Msgs
        message = client.messages.create(
            body=content,
            from_=f"whatsapp:{env.TWILIO_FROM_NUMBER}",
            to=f"whatsapp:{env.TWILIO_TO_NUMBER}",
        )
        print(message.status)
