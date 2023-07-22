from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    im = browser.find_element(By.ID, "treasure")
    x = im.get_attribute("valuex")
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    anws = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, "[type = 'checkbox']").click()
    option2 = browser.find_element(By.CSS_SELECTOR, "[value = 'robots']").click()
    button = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']").click()
finally:
    time.sleep(5)
    browser.quit()
