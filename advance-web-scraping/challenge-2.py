from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Wait for element to be located max until 10s
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#articlecount a"))
)

article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a").text
print(article_count)

# Wait for search bar element
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "search"))
)

search_input = driver.find_element(By.NAME, value="search")
search_input.send_keys("Marvel", Keys.ENTER)

time.sleep(10)

driver.quit()
