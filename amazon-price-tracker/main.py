import requests
from bs4 import BeautifulSoup
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("PASSWORD")

PRODUCT_URL = "https://www.amazon.com/Apple-2023-MacBook-512GB-Storage/dp/B0CB9BWMPY/ref=sr_1_3_mod_primary_new?keywords=macbook+air+15+inch&sr=8-3&language=en_US&currency=INR"

response = requests.get(PRODUCT_URL)
html_contents = response.text

# IN $
PRESET_PRICE = 100

message = MIMEMultipart()
message["From"] = MY_EMAIL
message["To"] = MY_EMAIL
message["Subject"] = "Price drop alert!"


soup = BeautifulSoup(html_contents, "html.parser")

price_tag = soup.select_one("div span span.a-offscreen")
price = "".join(price_tag.getText()[1::].split(","))
img_tag = soup.select_one("#landingImage")
img_src = img_tag.get("src")
product_title = soup.title.string


html = f"""\
    <html>
        <body>
            <h2>{product_title}</h2>
            <img src={img_src} alt={product_title}/>
            <p>Price has been drop out to <span style={"font-weight: bold;"}>{price_tag.getText()}</span>, Checkout your product</p>
            <p>
                <a href={PRODUCT_URL}>{PRODUCT_URL}</a>
            </p>
        </body>
    </html>
    """
message.attach(MIMEText(html, "html"))

if float(price) <= PRESET_PRICE:
    # Notify through email
    with SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.send_message(message)
