from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

USERNAME = "better.coding"
PASSWORD = "Prayas1234@"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

driver.get("https://www.instagram.com/")
time.sleep(2)

username = driver.find_element(By.NAME, "username")
username.clear()
username.send_keys(USERNAME)
time.sleep(1)
password = driver.find_element(By.NAME, "password")
password.clear()
password.send_keys(PASSWORD)
time.sleep(1)

login = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login.click()

time.sleep(35)
driver.get("https://www.instagram.com/coders.learning/")
time.sleep(20)
follower_ele = driver.find_element(By.PARTIAL_LINK_TEXT, "followers")
follower_ele.click()

follow_buttons = driver.find_elements(By.CSS_SELECTOR, "button[type='button']")

for follow_btn in follow_buttons:
    print(follow_btn.text)