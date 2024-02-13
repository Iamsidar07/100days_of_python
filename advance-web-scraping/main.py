from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.amazon.in/Apple-2023-MacBook-Laptop-chip/dp/B0C75GV58R/ref=sr_1_3?keywords=macbook+air+m2+15"
           "+inch&sr=8-3")

price_symbol = driver.find_element(By.CLASS_NAME, "a-price-symbol")
price = driver.find_element(By.CLASS_NAME, "a-price-whole")

print({price, price_symbol})

search = driver.find_element(By.NAME, value="field-keywords")
search.send_keys("Macbook air 15 inch", Keys.ENTER)

add_to_cart = driver.find_element(By.ID, value="add-to-cart-button")
add_to_cart.click()

buy_now = driver.find_element(By.ID, value="buy-now-button")
buy_now.click()

driver.quit()
