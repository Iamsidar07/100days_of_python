from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import ElementClickInterceptedException

USERNAME = ""
PASSWORD = ""

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
search_btn = driver.find_element(By.PARTIAL_LINK_TEXT, "Search")
search_btn.click()
time.sleep(5)

search_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search']")
search_input.send_keys("Coding")
time.sleep(5)

account_ele = driver.find_element(By.CSS_SELECTOR, ".x78zum5 a")
account_ele.click()

time.sleep(60)
follower_ele = driver.find_element(By.PARTIAL_LINK_TEXT, "followers")
follower_ele.click()
time.sleep(10)
followers_container = driver.find_element(By.CLASS_NAME, "_aano")
scroll_origin = ScrollOrigin.from_element(followers_container)
ActionChains(driver) \
    .scroll_from_origin(scroll_origin, 0, 1000) \
    .perform()
time.sleep(5)

follow_buttons = driver.find_elements(By.CSS_SELECTOR, "._aano button")
print(len(follow_buttons))
for follow_btn in follow_buttons:
    time.sleep(1)
    if follow_btn.text == "Follow":
        try:
            follow_btn.click()
        except ElementClickInterceptedException:
            print("Something went wrong!")
