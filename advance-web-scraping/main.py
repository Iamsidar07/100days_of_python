from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.amazon.in/')

title = driver.title

driver.implicitly_wait(0.5)

search_input = driver.find_element(By.NAME, value="field-keywords")
search_input.send_keys("Macbook air 15 inch", Keys.ENTER)

driver.implicitly_wait(0.5)

amazon_choice_product = driver.find_element(By.CLASS_NAME, value="a-badge-region")
amazon_choice_product.click()

driver.implicitly_wait(0.5)

product_title = driver.find_element(By.ID, value="productTitle").text

add_to_cart = driver.find_element(By.CLASS_NAME, value=".add-to-cart")
print(add_to_cart.click())

driver.quit()
