# module 2 lesson 1 step 7

# full task:
# В данной задаче вам нужно с помощью роботов решить ту же математическую задачу, как и в прошлом задании. 
# Но теперь значение переменной х спрятано в "сундуке", точнее, значение хранится в атрибуте valuex у картинки с изображением сундука.
# Ваша программа должна выполнить следующие шаги:
# 1. Открыть страницу http://suninjuly.github.io/get_attribute.html.
# 2. Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
# 3. Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
# 4. Посчитать математическую функцию от x (сама функция остаётся неизменной).
# 5. Ввести ответ в текстовое поле.
# 6. Отметить checkbox "I'm the robot".
# 7. Выбрать radiobutton "Robots rule!".
# 8. Нажать на кнопку Submit.

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
    browser.get("http://suninjuly.github.io/get_attribute.html")

    x_element = browser.find_element(By.ID, 'treasure')
    x = x_element.get_attribute('valuex')
    y = calc(x)

    input4 = browser.find_element(By.ID, 'answer')
    input4.send_keys(y)
    option1 = browser.find_element(By.ID, 'robotCheckbox')
    option1.click()
    option2 = browser.find_element(By.ID, 'robotsRule')
    option2.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
