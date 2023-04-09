import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time


# my credentials
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")


# driver path
chrome_driver_path = "C:\Development\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = Service(executable_path=chrome_driver_path)
driver = WebDriver(service=service, options=options)
driver.maximize_window()

driver.get("https://www.datemyage.com/en/people/#live")
time.sleep(5)


# Account sign in
email = driver.find_element(By.ID, ':r0:')
email.send_keys(MY_EMAIL)

password = driver.find_element(By.ID, ':r1:')
password.send_keys(MY_PASSWORD)
password.send_keys(Keys.ENTER)

time.sleep(10)


# Tapping into the first stream
first_stream = driver.find_element(By.CSS_SELECTOR, '.aafaba li')
first_stream.click()
time.sleep(2)

layout_on_button = driver.find_elements(By.CSS_SELECTOR, '._14d8ff ._3e89c9')[1]
layout_on_button.click()

time.sleep(10)

layout_off_button = driver.find_elements(By.CSS_SELECTOR, '._14d8ff ._3e89c9')[1]
layout_off_button.click()
time.sleep(2)


# swiping streams
start_time = time.time()
while True:

    try:
        next_stream = driver.find_element(By.CSS_SELECTOR, '.streaming-popup-desktop ._442b20')
        next_stream.click()
        time.sleep(2)

        layout_on_button = driver.find_elements(By.CSS_SELECTOR, '._14d8ff ._3e89c9')[1]
        layout_on_button.click()

    except selenium.common.exceptions.NoSuchElementException:
        print("That's all there is to it!")
        break

    else:
        time.sleep(10)

        layout_off_button = driver.find_elements(By.CSS_SELECTOR, '._14d8ff ._3e89c9')[1]
        layout_off_button.click()
        time.sleep(2)

    if time.time() - start_time > 300:
        break


print("That's enough, go do something better")
