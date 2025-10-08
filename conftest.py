#!/usr/bin/python3
import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="module")
def browser():
    #chrome_path = "/home/josivan/Downloads/chrome-linux64/chrome"
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.binary_location = chrome_path
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    yield driver
    driver.quit()
