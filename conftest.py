#!/usr/bin/python3
import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome('/home/josivan/Downloads/ChromeDriver/chromedriver-linux64/chromedriver')

    yield driver
    driver.quit()
