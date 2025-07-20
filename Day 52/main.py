import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

load_dotenv()

SIMILAR_ACCOUNT = "cristiano"
USERNAME = os.environ["INSTAGRAM_USERNAME"]
PASSWORD = os.environ["PASSWORD"]


class InstaFollower:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        url = "https://www.instagram.com/accounts/login/"
        self.driver.get(url)
        time.sleep(5)

        decline_cookies_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]"
        cookie_warning = self.driver.find_elements(By.XPATH, decline_cookies_xpath)
        if cookie_warning:
            cookie_warning[0].click()

        username = self.driver.find_element(by=By.NAME, value="username")
        password = self.driver.find_element(by=By.NAME, value="password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(3)
        password.send_keys(Keys.ENTER)

        time.sleep(8)
        save_login_prompt = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
        if save_login_prompt:
            save_login_prompt.click()

        time.sleep(4)
        # notifications_prompt = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Not Now')]")
        # if notifications_prompt:
        #     notifications_prompt.click()

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        time.sleep(8)
        followers_link = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'followers')
        followers_link.click()
        time.sleep(6)
        modal_xpath = "/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]"
        modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)
        for i in range(5):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as an HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        print("In Follow")
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._acap button')
        print(all_buttons)
        for button in all_buttons:
            print("following")
            try:
                button.click()
                time.sleep(1.1)
            # Clicking button for someone who is already being followed will trigger dialog to Unfollow/Cancel
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
