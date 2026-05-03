from typing import Literal

import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from curl import *
import urls
from locators import Locators
MAIN_PAGE = urls.main_site
REG_PAGE = urls.register_url
FORGOT_PASSWORD_PAGE = urls.forgot_password_url

class TestBurgerConstructor:

    @pytest.mark.parametrize("first_tab, second_tab, expected_name", [
        (Locators.SAUCES_SECTION, Locators.BUNS_SECTION, "Булки"),
        (Locators.BUNS_SECTION, Locators.SAUCES_SECTION, "Соусы"),
        (Locators.BUNS_SECTION, Locators.FILLINGS_SECTION, "Начинки")
    ], ids=["Bulki", "Souses", "Nachinki"])

    def test_burger_constructor_choosing_tabs(self, driver: WebDriver,
                                              first_tab: tuple[ByType, Literal['//h2[text()="Соусы"]//following-sibling::ul']] |
                                                         tuple[ByType, Literal['//h2[text()="Начинки"]//following-sibling::ul']] |
                                                         tuple[ByType, Literal['//h2[text()="Булки"]//following-sibling::ul']],
                                              second_tab: tuple[ByType, Literal['//h2[text()="Булки"]//following-sibling::ul']] |
                                                          tuple[ByType, Literal['//h2[text()="Соусы"]//following-sibling::ul']] |
                                                          tuple[ByType, Literal['//h2[text()="Начинки"]//following-sibling::ul']],
                                              expected_name: Literal['Булки'] | Literal['Соусы'] | Literal['Начинки']):
        driver.get(MAIN_PAGE)

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(first_tab)).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(second_tab)).click()

        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ACTIVE_TAB)).text == expected_name