# module 2 lesson 2 step 8

# full task:
# В этом задании в форме регистрации требуется загрузить текстовый файл. 
# Напишите скрипт, который будет выполнять следующий сценарий:
# 1. Открыть страницу http://suninjuly.github.io/file_input.html
# 2. Заполнить текстовые поля: имя, фамилия, email
# 3. Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
# 4. Нажать на кнопку "Submit"

# Remember!
# code will be useless after 30 seconds

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://SunInJuly.github.io/execute_script.html")

    input1 = browser.find_element(By.NAME, 'firstname')
    input1.send_keys("Alex")
    input2 = browser.find_element(By.NAME, 'lastname')
    input2.send_keys("Zaurovna")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("Smolensk")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
