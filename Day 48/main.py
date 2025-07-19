from selenium import webdriver
from selenium.webdriver.common.by import By

# keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.in/PlayStation%C2%AE5-Console-STD-SLIM-Bundle/dp/B0FG835ZCY/ref=sr_1_1")
driver.get("https://www.python.org")

# frame_1 = driver.find_element(By.CLASS_NAME, "a-button-text")
# frame_1.click()
#
# price_inr = driver.find_element(By.CLASS_NAME, "a-price-whole")
# print(f"The price is {price_inr.text}")

# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, "submit")
# print(button.size)
# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)

# XPath
# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

# driver.find_elements()

driver.close()  # closes the active tab
# driver.quit() # closes the entire window
