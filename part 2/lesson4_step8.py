# module 2 lesson 3 step 6

# full task:
# Написать программу,
# которая будет бронировать нам дом для отдыха по строго заданной цене.
# Более высокая цена нас не устраивает,
# а по более низкой цене объект успеет забронировать кто-то другой.

# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
# 1. Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# 2. Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# 3. Нажать на кнопку "Book"
# 4. Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение

# Remember!
# code will be useless after 30 seconds

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    
    button1 = browser.find_element(By.ID, "book")
    button1.click()

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    button2 = browser.find_element(By.ID, "solve")
    button2.click()

finally:
    time.sleep(30)
    browser.quit()
