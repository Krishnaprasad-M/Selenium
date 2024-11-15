from selenium import webdriver

def test_sample():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    print(driver.title)
    assert driver.title=="Login - VWO"
    assert driver.current_url== "https://app.vwo.com/#/login"