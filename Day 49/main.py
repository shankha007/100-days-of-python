from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os
from dotenv import load_dotenv
from time import sleep

load_dotenv()

def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(os.environ["URL"])
sleep(2)

sign_in_btn = driver.find_element(By.XPATH,
                                  '//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
sign_in_btn.click()

email_input = driver.find_element(By.XPATH, '//*[@id="base-sign-in-modal_session_key"]')
email_input.send_keys(os.environ["EMAIL"])

password_input = driver.find_element(By.XPATH, '//*[@id="base-sign-in-modal_session_password"]')
password_input.send_keys(os.environ["PASSWORD"])

sign_in = driver.find_element(By.XPATH, '//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button')
sign_in.click()
# CAPTCHA - Solve Puzzle Manually
input("Press Enter when you have solved the Captcha")

# Get Listings
sleep(5)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

for listing in all_listings:
    print("Opening Listing")
    listing.click()
    sleep(2)
    try:
        # Click Easy Apply Button
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-apply-button")
        if apply_button.text == "Easy Apply":
            apply_button.click()
        else:
            continue

        sleep(5)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys(os.environ["MOBILE_NUMBER"])

        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            # Click Submit Button
            print("Submitting job application")
            submit_button.click()

        sleep(2)
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue

sleep(5)
driver.quit()