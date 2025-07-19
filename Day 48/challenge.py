from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

menu = driver.find_element(By.CSS_SELECTOR, ".event-widget .menu")
events = menu.find_elements(By.TAG_NAME, "li")
event_dictionary = {}
for i in range(len(events)):
    event_dictionary[i] = {"time": events[i].find_element(By.TAG_NAME, "time").text,
                           "name": events[i].find_element(By.TAG_NAME, "a").text}

print(event_dictionary)

driver.close()
