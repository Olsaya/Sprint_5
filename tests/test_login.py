from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import LoginInfo
from locators import Locators
from curl import *

MAIN_PAGE = "https://stellarburgers.education-services.ru/"
REG_PAGE = "https://stellarburgers.education-services.ru/register"
FORGOT_PASSWORD_PAGE = "https://stellarburgers.education-services.ru/forgot-password"

class TestLogin:

    def test_login_main_page(self, driver):
        driver.get(MAIN_PAGE)
        driver.find_element(*Locators.MAIN_LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.EMAIL)).send_keys(LoginInfo.email)
        driver.find_element(*Locators.PASSWORD).send_keys(LoginInfo.password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_TITLE))
        assert driver.current_url == MAIN_PAGE

    def test_login_profile_page(self, driver):
        driver.get(MAIN_PAGE)
        driver.find_element(*Locators.PROFILE_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.EMAIL)).send_keys(LoginInfo.email)
        driver.find_element(*Locators.PASSWORD).send_keys(LoginInfo.password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_TITLE))
        assert driver.current_url == MAIN_PAGE

    def test_login_registration_page(self, driver):
        driver.get(REG_PAGE)
        driver.find_element(*Locators.SIGN_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.EMAIL)).send_keys(LoginInfo.email)
        driver.find_element(*Locators.PASSWORD).send_keys(LoginInfo.password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_TITLE))
        assert driver.current_url == MAIN_PAGE

    def test_login_forgot_password_page(self, driver):
        driver.get(FORGOT_PASSWORD_PAGE)
        driver.find_element(*Locators.SIGN_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.EMAIL)).send_keys(LoginInfo.email)
        driver.find_element(*Locators.PASSWORD).send_keys(LoginInfo.password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_TITLE))
        assert driver.current_url == MAIN_PAGE
        