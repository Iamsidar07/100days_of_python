from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

TIMEOUT = 5

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=chrome_options)
browser.maximize_window()

URL = "https://orteil.dashnet.org/cookieclicker/"

browser.get(URL)

WebDriverWait(driver=browser, timeout=10).until(
    EC.presence_of_element_located((By.ID, "langSelect-EN"))
)
lang_select = browser.find_element(By.ID, "langSelect-EN")
lang_select.click()

WebDriverWait(driver=browser, timeout=10).until(
    EC.presence_of_element_located((By.ID, "bigCookie"))
)
cookie = browser.find_element(By.ID, "bigCookie")

while True:
    start_time = time.time()
    while time.time() - start_time < TIMEOUT:
        cookie.click()

    WebDriverWait(driver=browser, timeout=10).until(
        EC.presence_of_element_located((By.ID, "cookies"))
    )
    # cookie count
    cookie_count = int(browser.find_element(By.ID, "cookies").text.split()[0])

    WebDriverWait(driver=browser, timeout=10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "price"))
    )
    store_products = browser.find_elements(By.CLASS_NAME, "price")
    prices = [int("".join(product.text.split(","))) for product in store_products if len(product.text) != 0]
    print(prices)
    for price in prices:
        if cookie_count >= price:
            prod_ele = browser.find_element(By.CSS_SELECTOR, f"#product{prices.index(price)}.unlocked")
            prod_ele.click()
            cookie_count -= price
    time.sleep(2)
