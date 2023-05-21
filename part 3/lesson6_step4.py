# module 3 lesson 6 step 4

# full task:
# открыть в Chrome урок по ссылке https://stepik.org/lesson/236895/step/1
# авторизоваться со своими логином и паролем 
# дождаться того, что поп-апа с авторизацией больше нет


import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def check_page(link): 
    browser = webdriver.Chrome()
    browser.get(link)
    return browser

def form_open(browser):
    btnOpenPopupWait = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "navbar__auth_login"))
    )
    btnOpenPopup = browser.find_element(By.CLASS_NAME, "navbar__auth_login")
    btnOpenPopup.click()

def form_fill(browser, login, password):
    popup = browser.find_element(By.CLASS_NAME, 'modal-dialog__content')
    fillLogin = popup.find_element(By.ID, 'id_login_email')
    fillLogin.send_keys(login)
    fillPaswd = popup.find_element(By.ID, 'id_login_password')
    fillPaswd.send_keys(password)
    return popup

def form_send(popup):
    btnSendForm = popup.find_element(By.CLASS_NAME, "sign-form__btn")
    btnSendForm.click()

class TestLogin(unittest.TestCase):
    def test_login_form(self):
        link = "https://stepik.org/lesson/236895/step/1"
        login = "your_login"
        password = "your_password"
        browser=check_page(link)
        form_open(browser)
        popup = form_fill(browser, login, password)
        form_send(popup)

if __name__ == "__main__":
    unittest.main()