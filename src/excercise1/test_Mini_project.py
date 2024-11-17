'''
Open the Url - ﻿www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067

Search for the Macmini

Click on the search ICON

Get all the titles

Get al the prices

Print all the titles and prices in the end. (side by side)

Find the Max and Min price also (from the list)
'''
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_mini_project():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")
    driver.find_element(By.XPATH, "//input[@class = 'gh-tb ui-autocomplete-input']").send_keys("MACMINI")
    driver.find_element(By.XPATH, "//input[@class='btn btn-prim gh-spr']").click()
    time.sleep(3)
    titles = driver.find_elements(By.CSS_SELECTOR, ".s-item__title")
    prices = driver.find_elements(By.CSS_SELECTOR, ".s-item__price")
    l = len(titles)

    for title, price in zip(titles, prices):
        print(f"Title: {title.text} - Price: {price.text}")



