# module 1 lesson 6 step 11

# full task:
# Тест успешно проходит на странице http://suninjuly.github.io/registration1.html
# Тест падает с ошибкой NoSuchElementException http://suninjuly.github.io/registration2.html
# Используемые селекторы должны быть уникальны

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    # link = "http://suninjuly.github.io/registration1.html"
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    required = browser.find_element(By.CLASS_NAME, 'first_block')
    input1 = required.find_element(By.CLASS_NAME, 'first')
    input1.send_keys("Ivan")
    input2 = required.find_element(By.CLASS_NAME, 'second')
    input2.send_keys("Petrov")
    input3 = required.find_element(By.CLASS_NAME, 'third')
    input3.send_keys("test@tes.te")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()

# selector idea from another student:
# browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.first_class > input')

# comments from reveiws:
# """
# в целом норм, но... 
# можно было создать список из линков и пройтись по ним в цикле,
# например: for link in links: browser.get(link) 
# а также завести блок except try: ... except Exception as ex: print(ex) finally: ...
# """
# and
# """
# в целом норм, но... 
# в место длинного ряда селекторов можно и покороче, 
# например: '.first_block .first' 
# а также завести создать список уникальных селекторов и пройтись по ним в цикле, например: 
# uniq_selectors = ('.first', '.second', '.third') 
# for u in uniq_selectors: 
# element = browser.find_element(By.CSS_SELECTOR, '.first_block ' + u)
# element.send_keys('My answer')
# """