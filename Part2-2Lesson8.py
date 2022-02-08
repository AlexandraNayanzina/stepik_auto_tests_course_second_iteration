from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("Alex")
    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("Nayanzina")
    email_user = browser.find_element(By.NAME, "email")
    email_user.send_keys("test@test.test")
    choose_file_btn = browser.find_element(By.ID, "file")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'text.txt')
    choose_file_btn.send_keys(file_path)

    time.sleep(2)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(5)
    browser.quit()
