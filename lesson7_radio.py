from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    anws = browser.find_element(By.CSS_SELECTOR, "#answer")
    anws.send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, "[type = 'checkbox']").click()

    option2 = browser.find_element(By.CSS_SELECTOR, "[value = 'robots']").click()

    button = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']").click()
finally:
    time.sleep(10)
    browser.quit()
