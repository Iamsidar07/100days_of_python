import requests
from twilio.rest import Client
import os

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
from_ = os.environ.get("FROM_")
to = os.environ.get("TO")
stock_api_key = os.environ.get("STOCK_API_KEY")
news_api_key = os.environ.get("NEWS_API_KEY")

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

client = Client(account_sid, auth_token)


def get_stock_price_change():
    stock_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_NAME,
        "apikey": stock_api_key,
    }
    response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
    response.raise_for_status()
    data = response.json()["Time Series (Daily)"]
    stock_data = [value for (_key, value) in data.items()]
    yesterday_closing_price = float(stock_data[0]["4. close"])
    day_before_yesterday_closing_price = float(stock_data[1]["4. close"])
    diff_percentage = (
        (yesterday_closing_price - day_before_yesterday_closing_price)
        / yesterday_closing_price
        * 100
    )
    return diff_percentage


def get_news():
    news_params = {
        "qInTitle": COMPANY_NAME,
        "apikey": news_api_key,
    }
    response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    response.raise_for_status()
    articles = response.json()["articles"]
    top_articles = [
        {"headline": item["title"], "description": item["description"]}
        for item in articles[:3]
    ]
    return top_articles


def format_msg(msg, change):
    if change >= 0:
        sign = "🔺"
    else:
        sign = "🔻"
    return f"{STOCK_NAME}: {sign}{round(change, 2)}%\nHeadline: {msg['headline']}\nBrief: {msg['description']}"


percentage_change = get_stock_price_change()
if abs(percentage_change) >= 5:
    messages = get_news()
    for message in messages:
        message = client.messages.create(
            from_=from_, to=to, body=format_msg(msg=message, change=percentage_change)
        )
        print(message.status)
