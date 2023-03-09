# module 2 lesson 2 step 6

# full task:
# В данной задаче вам нужно будет снова преодолеть капчу для роботов и справиться с ужасным и огромным футером, 
# который дизайнер всё никак не успевает переделать. 
# Вам потребуется написать код, чтобы:
# 1. Открыть страницу http://SunInJuly.github.io/execute_script.html
# 2. Считать значение для переменной x
# 3. Посчитать математическую функцию от x
# 4. Проскроллить страницу вниз
# 5. Ввести ответ в текстовое поле
# 6. Выбрать checkbox "I'm the robot"
# 7. Переключить radiobutton "Robots rule!"
# 8. Нажать на кнопку "Submit"

# Remember!
# code will be useless after 30 seconds

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://SunInJuly.github.io/execute_script.html")

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    input4 = browser.find_element(By.ID, 'answer')
    input4.send_keys(y)
    option1 = browser.find_element(By.ID, 'robotCheckbox')
    option1.click()
    option2 = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
