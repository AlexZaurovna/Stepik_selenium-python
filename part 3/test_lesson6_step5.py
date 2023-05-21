# module 3 lesson 6 step 5

# full task:
# открыть в Chrome урок по ссылке https://stepik.org/lesson/236895/step/1
# авторизоваться со своими логином и паролем 
# дождаться того, что поп-апа с авторизацией больше нет

# P.S.
# It works correct without 'time.sleep()'
# But if you need to rerun this it usefull

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def form_open(browser):
    btnOpenPopupWait = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "navbar__auth_login"))
    )
    btnOpenPopup = browser.find_element(By.CLASS_NAME, "navbar__auth_login")
    btnOpenPopup.click()

def login_form_fill(browser, login, password):
    popup = browser.find_element(By.CLASS_NAME, 'modal-dialog__content')
    fillLogin = popup.find_element(By.ID, 'id_login_email')
    fillLogin.send_keys(login)
    fillPaswd = popup.find_element(By.ID, 'id_login_password')
    fillPaswd.send_keys(password)
    return popup

def login_form_send(popup):
    btnSendForm = popup.find_element(By.CLASS_NAME, "sign-form__btn")
    btnSendForm.click()
    time.sleep(10)

def answer_calc():
    answer = math.log(int(time.time()))
    return answer

def check_answer(browser):
    answer = answer_calc()
    time.sleep(10)
    answerInput = browser.find_element(By.CLASS_NAME, 'string-quiz__textarea')
    answerInput.send_keys(answer)
    answerSubmit = browser.find_element(By.CLASS_NAME, 'submit-submission')
    answerSubmit.click()
    feedback = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'smart-hints__hint'))
    ).text
    return feedback

# def get_UFO_Message(feedback):
#     UFOmessage = UFOmessage + feedback
#     return UFOmessage

class TestLogin(unittest.TestCase):
    def test_find_UFO_message(self):
        link = "https://stepik.org/lesson/236895/step/1"
        links = [
            "https://stepik.org/lesson/236896/step/1",
            "https://stepik.org/lesson/236897/step/1",
            "https://stepik.org/lesson/236898/step/1",
            "https://stepik.org/lesson/236899/step/1",
            "https://stepik.org/lesson/236903/step/1",
            "https://stepik.org/lesson/236904/step/1",
            "https://stepik.org/lesson/236905/step/1"
        ]
        login = "AlexZaurovna@yandex.ru"
        password = "_mi_St3p1k_"

        browser = webdriver.Chrome()
        browser.get(link)
        form_open(browser)
        popup = login_form_fill(browser, login, password)
        login_form_send(popup)
        feedback = check_answer(browser)
        if (feedback != "Correct!"):
            print(feedback)

        for link in links:
            browser.get(link)
            feedback = check_answer(browser)
            # if (self.assertEqual("Correct!", feedback) != True):
            if (feedback != "Correct!"):
                # UFOmessage = get_UFO_Message(feedback)
                print(feedback)
            # print(UFOmessage)

if __name__ == "__main__":
    unittest.main()