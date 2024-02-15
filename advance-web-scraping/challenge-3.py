from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

FNAME = "someone"
LNAME = "SOMEHOW"
EMAIL = "DONTKNOW@GMAIL.COM"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.maximize_window()

URL = "http://secure-retreat-92358.herokuapp.com/"
driver.get(URL)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "fName"))
)

fname = driver.find_element(By.NAME, "fName")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "lName"))
)
lname = driver.find_element(By.NAME, "lName")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "email"))
)
email = driver.find_element(By.NAME, "email")

fname.clear()
fname.send_keys(FNAME)
lname.clear()
lname.send_keys(LNAME)
email.clear()
email.send_keys(EMAIL)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']"))
)

submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
submit_btn.click()

time.sleep(10)

driver.quit()
