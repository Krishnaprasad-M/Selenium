from  selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_alert_normal():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.find_element(By.XPATH,"//button[@onclick='jsAlert()']").click()
    WebDriverWait(driver=driver,timeout=5,poll_frequency=1).until(EC.alert_is_present())
    alert=driver.switch_to.alert
    alert.accept()
    result = driver.find_element(By.ID, "result")
    assert result.text == "You successfully clicked an alert"
    time.sleep(5)

def test_alert_confirm():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']").click()
    WebDriverWait(driver=driver, timeout=5, poll_frequency=1).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.dismiss()
    result=driver.find_element(By.ID,"result")
    assert result.text == "You clicked: Cancel"

    time.sleep(5)
def test_alert_prompt():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']").click()
    WebDriverWait(driver=driver, timeout=5, poll_frequency=1).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.send_keys("Krishna")
    alert.accept()
    result = driver.find_element(By.ID, "result")
    assert result.text == "You entered: Krishna"

    time.sleep(5)
