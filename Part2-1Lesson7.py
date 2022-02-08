from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    checkbox = browser.find_element(By.ID, "robotCheckbox").click()
    radio = browser.find_element(By.ID,("robotsRule")).click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(3)
    browser.quit()
