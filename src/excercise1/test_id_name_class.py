import allure
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

@allure.title("Locators testing")
@allure.description("negative tc")
def testvwo_id_name_class():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    driver.find_element(By.ID,"login-username").send_keys("abc@gmail.com")
    driver.find_element(By.NAME,"password").send_keys("senditda")
    driver.find_element(By.ID,"js-login-btn").click()
    error=driver.find_element(By.CLASS_NAME,"notification-box-description")
    time.sleep(5)
    print(error.text)
    assert error.text == "Your email, password, IP address or location did not match"
    driver.find_element(By.PARTIAL_LINK_TEXT,"free trial").click()
    assert driver.current_url == "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"