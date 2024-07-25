from time import sleep

import allure
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class TestExample:
    @allure.title('Test Example')
    @pytest.mark.smoke
    def test_example(self, browser):
        with allure.step("Step1. В поисковике google вводим текст 'Скуф' и кликаем по кнопке ENTER"):
            browser.get('https://www.google.ru/?hl=ru')
            search_row_locator = browser.find_element(By.CSS_SELECTOR, 'textarea[name="q"]')
            search_row_locator.send_keys('скуф')
            search_row_locator.send_keys(Keys.ENTER)
            title_of_searching_page_locator = browser.find_element(By.CSS_SELECTOR, 'div[data-attrid="title"]')
            title_of_page_text = title_of_searching_page_locator.text
        with allure.step("Assert. Заголовок страницы соответствует 'Скуф'"):
            assert title_of_page_text == 'Скуф'
