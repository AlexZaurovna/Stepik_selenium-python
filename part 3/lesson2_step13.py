# module 3 lesson 2 step 13

# full task:
# переоформление тестов из первого модуля в стиле unittest
# 1. Возьмите тесты из шага — https://stepik.org/lesson/138920/step/11?unit=196194
# 2. Создайте новый файл
# 3. Создайте в нем класс с тестами, который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом
# 4. Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
# 5. Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
# 6. Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
# 7. Запустите получившиеся тесты из файла 
# 8. Просмотрите отчёт о запуске и найдите последнюю строчку 
# 9. Отправьте эту строчку в качестве ответа на это задание 

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_check_page(link): 
    browser = webdriver.Chrome()
    browser.get(link)
    return browser

def test_form_fill(browser):
    required = browser.find_element(By.CLASS_NAME, 'first_block')
    input1 = required.find_element(By.CLASS_NAME, 'first')
    input1.send_keys("Ivan")
    input2 = required.find_element(By.CLASS_NAME, 'second')
    input2.send_keys("Petrov")
    input3 = required.find_element(By.CLASS_NAME, 'third')
    input3.send_keys("test@tes.te")

def test_form_btn(browser):
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    return welcome_text

class TestRegister(unittest.TestCase):
    def test_registration_form_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser=test_check_page(link)
        test_form_fill(browser)
        welcome_text=test_form_btn(browser)
        self.assertEqual('Congratulations! You have successfully registered!', welcome_text)

    def test_registration_form_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser=test_check_page(link)
        test_form_fill(browser)
        welcome_text=test_form_btn(browser)
        self.assertEqual('Congratulations! You have successfully registered!', welcome_text)

if __name__ == "__main__":
    unittest.main()