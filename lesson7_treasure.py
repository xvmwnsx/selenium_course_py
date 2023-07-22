from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    im = browser.find_element(By.ID, "treasure")
    x = im.get_attribute("valuex")
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    anws = browser.find_element(By.CSS_SELECTOR, "#answer")
    anws.send_keys(y)

    option1 = browser.find_element(By.CSS_SELECTOR, "[type = 'checkbox']")
    option1.click()

    option2 = browser.find_element(By.CSS_SELECTOR, "[value = 'robots']")
    option2.click()

    button = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
