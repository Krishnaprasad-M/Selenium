from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def testcase_ID():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    makeapp = driver.find_element(By.ID,"btn-make-appointment")
    makeapp.click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    driver.find_element(By.ID,"txt-username").send_keys("John Doe")
    driver.find_element(By.ID,"txt-password").send_keys("ThisIsNotAPassword")
    log = driver.find_element(By.ID,"btn-login")
    log.click()
    msg = driver.current_url
    print(msg)
    assert msg == "https://katalon-demo-cura.herokuapp.com/#appointment"
