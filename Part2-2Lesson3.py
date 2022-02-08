from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1_text = browser.find_element(By.ID, "num1")
    num1 = int(num1_text.text)

    num2_text = browser.find_element(By.ID, "num2")
    num2 = int(num2_text.text)

    val = num1 + num2

    # browser.find_element(By.TAG_NAME, "select").click()
    # browser.find_element(By.CSS_SELECTOR, "[value=val]").click()

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(val))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(10)
    browser.quit()
