import allure
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

@allure.title("Automating Opencart")
@allure.description("Test case")
def test_xpath():
    chrop = Options()
    chrop.add_argument("--incognito")
    driver = webdriver.Chrome(chrop)
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")
    driver.find_element(By.XPATH,"//input[@id = 'input-firstname']").send_keys("Krishna")
    driver.find_element(By.XPATH,"//*[@placeholder = 'Last Name' and @id = 'input-lastname']").send_keys("Prasad")
    driver.find_element(By.XPATH,"//input[@name = 'email']").send_keys("krishnaprasad.m3@gmail.com")
    driver.find_element(By.XPATH, "//input[@name = 'telephone']").send_keys("98546737")
    driver.find_element(By.XPATH, "//input[@name = 'password']").send_keys("gulandu")
    driver.find_element(By.XPATH, "//input[@name = 'confirm']").send_keys("gulandu")
    driver.find_element(By.XPATH,"//input[@name = 'newsletter' and @value ='1']").click()
    driver.find_element(By.XPATH, "//input[@name = 'agree' and @value ='1']").click()
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    time.sleep(5)
    msg = driver.find_element(By.XPATH, "//div[@class= 'col-sm-9']/h1")
    print(msg.text)
    assert msg.text == "Your Account Has Been Created!"

