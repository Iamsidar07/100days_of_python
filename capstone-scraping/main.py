import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

GOOGLE_FORM_URL = (
    "https://docs.google.com/forms/d/e/1FAIpQLSf61aXS7KnPbwLQTbVHrY65ZZrfMCdaZTOfBC6cdjwj2CL2ig"
    "/viewform?usp=sf_link"
)
ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(ZILLOW_URL)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")
prices = [
    price.text
    for price in soup.select(selector=".PropertyCardWrapper__StyledPriceLine")
]
locs = [
    loc.text for loc in soup.select(selector=".StyledPropertyCardDataWrapper address")
]
urls = [
    url.get("href") for url in soup.select(selector=".StyledPropertyCardDataWrapper a")
]

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get(GOOGLE_FORM_URL)
time.sleep(2)

for i in range(0, len(prices)):
    prop_address = driver.find_element(
        By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div['
        "2]/div/div[1]/div/div[1]/input",
    )
    prop_price = driver.find_element(
        By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div['
        "1]/div/div[1]/input",
    )
    prop_url = driver.find_element(
        By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div['
        "1]/div/div[1]/input",
    )
    button = driver.find_element(By.CLASS_NAME, "uArJ5e")
    prop_address.send_keys(locs[i].strip())
    price = prices[i]
    if "+" in price:
        price = price.split("+")
    elif "/" in price:
        price = price.split("/")
    prop_price.send_keys(price[0])
    prop_url.send_keys(urls[i])
    button.click()
    time.sleep(3)
    submit_another_response = driver.find_element(
        By.LINK_TEXT, "Submit another response"
    )
    submit_another_response.click()
    time.sleep(3)
