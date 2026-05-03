import pytest

from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from curl import *
from data import *
from locators import Locators

#  Подключаем webdriver для Chrome
@pytest.fixture(scope="function")
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()
    

@pytest.fixture(scope="function")
def driver_with_login():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(account_url)

    # Заходим в аккаунто пользователя
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
    
    browser.find_element(*Locators.LOGIN_EMAIL).send_keys(LoginInfo.email)
    browser.find_element(*Locators.LOGIN_PASSWORD).send_keys(LoginInfo.password)
    browser.find_element(*Locators.LOGIN_BUTTON).click()
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.ACCOUNT_HEADER_LINK))
    browser.find_element(*Locators.LOGO_HEADER_LINK).click()

    yield browser
    
    browser.quit()



   