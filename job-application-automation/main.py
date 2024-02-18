from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

EMAIL = ""
PASSWORD = ""

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=chrome_options)
browser.maximize_window()

time.sleep(1)
browser.get("https://www.linkedin.com/home")

WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, "session_key"))
)
WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, "session_password"))
)
WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-id='sign-in-form__submit-btn']"))
)

email_input = browser.find_element(By.ID, "session_key")
password_input = browser.find_element(By.ID, "session_password")
time.sleep(4)
email_input.clear()
email_input.send_keys(EMAIL)
time.sleep(4)
password_input.clear()
password_input.send_keys(PASSWORD)

login_btn = browser.find_element(By.CSS_SELECTOR, "button[data-id='sign-in-form__submit-btn']")
# login_btn.submit()
login_btn.click()

# login complete
time.sleep(2)
jobs_btn = browser.find_element(By.LINK_TEXT, "Jobs")
jobs_btn.click()

time.sleep(2)
WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "jobs-search-box__text-input"))
)

job_title_input = browser.find_element(By.CLASS_NAME, "jobs-search-box__text-input")
job_title_input.click()
job_title_input.clear()
job_title_input.send_keys("Marketing Intern")


WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "jobs-search-box__input--location"))
)

job_location_input = browser.find_element(By.CLASS_NAME, "jobs-search-box__input--location")
job_location_input.click()
job_location_input.clear()
job_location_input.send_keys("Remote", Keys.ENTER)

WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "button[area-label='Easy Apply filter.']"))
)

easy_apply_btn = browser.find_element(By.CSS_SELECTOR, "button[area-label='Easy Apply filter.']")
easy_apply_btn.click()

WebDriverWait(browser, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "job-card-container"))
)

job_containers = browser.find_elements(By.CLASS_NAME, "job-card-container")
for job_container in job_containers:
    job_container.click()
    WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "job-apply-button"))
)
    apply_job_btn = browser.find_element(By.CLASS_NAME, "job-apply-button")
    if apply_job_btn.is_enabled:
        apply_job_btn.click()
    else: 
        print("Disabled")
browser.quit()
