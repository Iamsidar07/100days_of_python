import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

USERNAME = ""
PASSWORD = ""
PROMISED_DOWN = 150
PROMISED_UP = 10


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "start-text"))
        )
        go = self.driver.find_element(By.CLASS_NAME, "start-text")
        go.click()
        time.sleep(60)
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "download-speed"))
        )
        download_speed = self.driver.find_element(By.CLASS_NAME, "download-speed")
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "upload-speed"))
        )
        upload_speed = self.driver.find_element(By.CLASS_NAME, "upload-speed")
        self.up = upload_speed.text
        self.down = download_speed.text

    def tweet_at_provider(self):
        time.sleep(5)
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(3)
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.NAME, "text"))
        )
        username = self.driver.find_element(By.NAME, "text")
        username.clear()
        username.send_keys(USERNAME, Keys.ENTER)
        time.sleep(5)
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password = self.driver.find_element(By.NAME, "password")
        password.clear()
        password.send_keys(PASSWORD, Keys.ENTER)
        time.sleep(20)

        compose_btn = self.driver.find_element(
            By.CSS_SELECTOR, "a[href='/compose/post']"
        )
        compose_btn.click()
        time.sleep(20)
        tweet_input = self.driver.find_element(
            By.XPATH,
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
            "2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div["
            "2]/div/div/div/div/div/div/div["
            "2]/div/div/div/div/label/div[1]/div/div/div/div/div/div["
            "2]/div",
        )

        tweet = f"""Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"""
        tweet_input.send_keys(tweet)
        time.sleep(3)
        tweet_btn = self.driver.find_element(
            By.CSS_SELECTOR, "div[data-testid='tweetButton']"
        )
        tweet_btn.click()
