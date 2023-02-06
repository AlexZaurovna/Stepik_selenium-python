# module 2 lesson 2 step 3

# full task:
# Напишите код, который реализует следующий сценарий:
# 1. Открыть страницу https://suninjuly.github.io/selects1.html
# 2. Посчитать сумму заданных чисел
# 3. Выбрать в выпадающем списке значение равное расчитанной сумме
# 4. Нажать кнопку "Submit"

# Remember!
# code will be useless after 30 seconds

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x, y):
    return str(x+y)

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects1.html")

    x_element = browser.find_element(By.ID, 'num1')
    x = int(x_element.text)
    y_element = browser.find_element(By.ID, 'num2')
    y = int(y_element.text)
    z = str(calc(x,y))

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(z)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
