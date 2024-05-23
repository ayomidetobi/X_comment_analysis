from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

web = "https://x.com/i/flow/login"
# C:\Users\HP\Downloads\chromedriver-win64\chromedriver-win64
path = "C:/Users/HP/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
# Open the URL
driver.get(web)
driver.maximize_window()

# Wait for the page to load
time.sleep(6)  # Adjust this time based on your computer's performance

# Locate username input and send text
username = driver.find_element(By.XPATH, '//input[@autocomplete ="username"]')
username.send_keys("username")  # Replace with your username

# Locate and click the "Next" button
next_button = driver.find_element(By.XPATH, '//div[@role="button"]//span[text()="Next"]')
next_button.click()

# Wait after clicking the button
time.sleep(2)

# Locate password input and send text
password = driver.find_element(By.XPATH, '//input[@autocomplete ="current-password"]')
password.send_keys("password")  # Replace with your password

# Locate and click the "Log in" button
login_button = driver.find_element(By.XPATH, '//div[@role="button"]//span[text()="Log in"]')
login_button.click()

# Optional: Close the driver
# driver.quit()