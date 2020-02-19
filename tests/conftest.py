import time
import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from time import sleep


@pytest.fixture()
def driver() -> WebDriver:
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)   # set max waiting time for all tests

    yield driver
    driver.close()




