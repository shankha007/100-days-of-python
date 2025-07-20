from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from time import sleep
import os
from dotenv import load_dotenv

load_dotenv()


class InternetSpeedTwitterBot:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = 0.0
        self.down = 0.0

    def get_internet_speed(self, url):
        self.driver.get(url)
        sleep(2)

        go_button = self.driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]/a')
        go_button.click()
        sleep(45)

        down_speed = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        up_speed = self.driver.find_element(By.CLASS_NAME, "upload-speed").text

        self.down = float(down_speed)
        self.up = float(up_speed)

    def tweet_at_provider(self, url):
        self.driver.get(url)
        sleep(2)

        sign_in_btn = self.driver.find_element(By.LINK_TEXT, "Sign in")
        sign_in_btn.click()
        sleep(4)

        email_input = self.driver.find_elements(By.CSS_SELECTOR, "input")[0]
        email_input.send_keys(os.environ["EMAIL"])
        sleep(1)

        next_btn = self.driver.find_elements(By.CSS_SELECTOR, "button")[2]
        next_btn.click()
        sleep(3)

        try:
            extra_screen = self.driver.find_element(By.ID, "modal-header")
            if extra_screen.text == "Enter your phone number or username":
                input_1 = self.driver.find_elements(By.CSS_SELECTOR, "input")[0]
                input_1.send_keys(os.environ["TWITTER_USERNAME"])
                sleep(1)

                next_btn_1 = self.driver.find_elements(By.CSS_SELECTOR, "button")[1]
                next_btn_1.click()
                sleep(2)
            else:
                raise NoSuchElementException

        except NoSuchElementException:
            pass

        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(os.environ["PASSWORD"])
        sleep(1)

        login_btn = self.driver.find_elements(By.CSS_SELECTOR, "button")[3]
        login_btn.click()
        sleep(5)

        tweet_compose = self.driver.find_element(By.XPATH,
                                                 value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {os.environ['PROMISED_DOWN']}down/{os.environ['PROMISED_UP']}up?"
        tweet_compose.send_keys(tweet)
        sleep(3)

        tweet_button = self.driver.find_element(By.XPATH,
                                                value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        tweet_button.click()

        sleep(2)
