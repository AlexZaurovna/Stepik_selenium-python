# module 2 lesson 3 step 6

# full task:
# В этом задании после нажатия кнопки страница откроется в новой вкладке,
# нужно переключить WebDriver на новую вкладку и решить в ней задачу.
# Сценарий для реализации выглядит так:
# 1. Открыть страницу http://suninjuly.github.io/redirect_accept.html
# 2. Нажать на кнопку
# 3. Переключиться на новую вкладку
# 4. Пройти капчу для робота и получить число-ответ

# Remember!
# code will be useless after 30 seconds

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    button1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button1.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    button2 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button2.click()

finally:
    time.sleep(30)
    browser.quit()