import pytest
from selenium import webdriver
import time
import allure


def test_sample_chrome():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    print(driver.title)
    assert driver.title == "Login - VWO"
    assert driver.current_url == "https://app.vwo.com/#/login"
    time.sleep(10)


def test_sample_edge():
    driver = webdriver.Edge()
    driver.get("https://app.vwo.com")
    print(driver.title)
    assert driver.title == "Login - VWO"
    assert driver.current_url == "https://app.vwo.com/#/login"
    time.sleep(10)
    driver.quit()
