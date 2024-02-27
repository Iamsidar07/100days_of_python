import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By

load_dotenv()

USERNAME = os.environ.get("username")
PASSWORD = os.environ.get("password")


class InstagramBot:
    def __init__(self) -> None:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        try:
            self.login(USERNAME, PASSWORD)
            time.sleep(5)
            self.search_by_keyword(keyword="Programming")
            time.sleep(5)
            self.click_on_account()
            time.sleep(5)
            self.follow_accounts()
            time.sleep(5)
        finally:
            self.driver.quit()

    def login(self, username, password):
        print("logging...")
        self.driver.get("https://www.instagram.com/")
        time.sleep(2)
        username_input = self.driver.find_element(By.NAME, "username")
        username_input.clear()
        username_input.send_keys(username)
        time.sleep(1)
        password_input = self.driver.find_element(By.NAME, "password")
        password_input.clear()
        password_input.send_keys(password)
        time.sleep(1)
        login = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login.click()

    def search_by_keyword(self, keyword):
        print("Searching for ", keyword)
        search_btn = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Search")
        search_btn.click()
        time.sleep(3)
        search_input = self.driver.find_element(
            By.CSS_SELECTOR, "input[placeholder='Search']"
        )
        search_input.send_keys(keyword)

    def click_on_account(self):
        print("Opening account...")
        account_ele = self.driver.find_element(By.CSS_SELECTOR, ".x78zum5 a")
        account_ele.click()
        time.sleep(60)

    def scroll_on_followers_list(self):
        print("Scrolling on followers list...")
        followers_container = self.driver.find_element(By.CLASS_NAME, "_aano")
        scroll_origin = ScrollOrigin.from_element(followers_container)
        ActionChains(self.driver).scroll_from_origin(scroll_origin, 0, 1000).perform()
        time.sleep(5)

    def follow_accounts(self):
        print("Following accounts...")
        follower_ele = self.driver.find_element(By.PARTIAL_LINK_TEXT, "followers")
        follower_ele.click()
        time.sleep(10)
        self.scroll_on_followers_list()
        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, "._aano button")
        for follow_btn in follow_buttons:
            time.sleep(1)
            if follow_btn.text == "Follow":
                try:
                    follow_btn.click()
                    print("Followed")
                except ElementClickInterceptedException:
                    print("Something went wrong!")
