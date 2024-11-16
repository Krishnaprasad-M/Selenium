from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import allure

def test_chromeoptions():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://www.pypi.org/project/allure-pytest/")
    time.sleep(10)
    driver.quit()