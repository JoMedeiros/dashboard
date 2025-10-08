#!/usr/bin/python3
import pytest
import time
from selenium import webdriver

@pytest.fixture(scope="module")
def browser():
    options = webdriver.FirefoxOptions()
    options.add_argument("-headless")
    driver = webdriver.Firefox(options=options)

    yield driver
    driver.quit()
