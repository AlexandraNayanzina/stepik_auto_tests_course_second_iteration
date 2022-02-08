from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
    first_name.send_keys("Ivan")

    last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
    last_name.send_keys("Petrov")

    user_email = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
    user_email.send_keys("test@test.test")

    user_phone = browser.find_element(By.CSS_SELECTOR, ".second_block .first")
    user_phone.send_keys("123456789")

    user_add = browser.find_element(By.CSS_SELECTOR, ".second_block .second")
    user_add.send_keys("test address")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(3)
    browser.quit()
