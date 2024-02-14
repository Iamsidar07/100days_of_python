from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from pprint import pprint

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.python.org/")

driver.implicitly_wait(0.5)

event_time_tags = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li time")
event_title_tags = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

event_dates = [event_time.get_attribute("datetime") for event_time in event_time_tags]
event_titles = [event_title.text for event_title in event_title_tags]
event_links = [event_title.get_attribute("href") for event_title in event_title_tags]

event_dict = {}
for i in range(len(event_dates)):
    new_event = {
            "link": event_links[i],
            "title":  event_titles[i],
            "time": event_dates[i].split("T")[0]
        }

    event_dict[i] = new_event

pprint(event_dict)
driver.quit()