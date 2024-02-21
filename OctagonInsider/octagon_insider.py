import random
import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from insider_news import InsiderNews

USERNAME = ""
PASSWORD = ""


class OctagonInsider:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.all_news = None

    def get_news(self):
        news_url = "https://www.mmafighting.com/"
        print("getting news..")
        response = requests.get(news_url)
        html_contents = response.text
        soup = BeautifulSoup(html_contents, "html.parser")
        news_elements = soup.select(selector=".c-entry-box--compact__title a")
        news_urls = [url.get("href") for url in news_elements]

        news_titles = [url.getText() for url in news_elements]
        all_news = []
        for i in range(len(news_elements)):
            new_news = InsiderNews(news_title=news_titles[i], news_url=news_urls[i])
            all_news.append(new_news)
        self.all_news = all_news

    def login_with_twitter(self):
        print("logging ...")
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

    def tweet_news(self):
        print("Tweeting...")
        news = random.choice(self.all_news)
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
        tweet = f"{news.title}\n\n{news.url}\n#OctagonInsider #ufc #mma "
        print(tweet)
        tweet_input.send_keys(tweet)
        time.sleep(3)
        tweet_btn = self.driver.find_element(
            By.CSS_SELECTOR, "div[data-testid='tweetButton']"
        )
        tweet_btn.click()
        time.sleep(15)

    def interact_with_tweets(self):
        print("Interacting...")
        like_btns = self.driver.find_elements(
            By.CSS_SELECTOR, "div[data-testid='like']"
        )
        retweet_btns = self.driver.find_elements(
            By.CSS_SELECTOR, "div[data-testid='retweet']"
        )
        more_btns = self.driver.find_elements(
            By.CSS_SELECTOR, "div[data-testid='caret']"
        )

        for i in range(len(like_btns)):
            random_chance = random.randint(1, 3)
            if random_chance == 1:
                like_btns[i].click()
                print("liked")
            elif random_chance == 2:
                more_btns[i].click()
                time.sleep(2)
                follow_btn = self.driver.find_element(
                    By.CSS_SELECTOR, "div[data-testid='Dropdown'] > div:nth-child(2)"
                )
                if "Follow" in follow_btn.text:
                    follow_btn.click()
                    print("Followed")
                time.sleep(1)

            else:
                retweet_btns[i].click()
                retweet_confirm = self.driver.find_element(
                    By.CSS_SELECTOR, "div[data-testid='retweetConfirm']"
                )
                retweet_confirm.click()
                print("retweet")
