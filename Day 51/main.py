import os
from dotenv import load_dotenv

from internet_speed_twitter_bot import InternetSpeedTwitterBot

load_dotenv()

bot = InternetSpeedTwitterBot()
should_complaint = bot.get_internet_speed("https://www.speedtest.net/")

if bot.down < float(os.environ["PROMISED_DOWN"]) or bot.up < float(os.environ["PROMISED_UP"]):
    bot.tweet_at_provider("https://x.com/")
