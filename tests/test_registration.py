import random

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants
from locators import Locators

new_email = f'kristina_naumova_4{random.randint(100, 999)}@yandex.ru'


class TestRegistration:
    def test_registration_positive(self, driver):
        # Клик по кнопке "Войти в аккаунт"
        driver.find_element(*Locators.BUTTON_PESONAL_ACCOUNT).click()

        WebDriverWait(driver, 5).until(EC.url_contains(Constants.LOGIN_URL))

        # Клик по тексту "Зарегистрироваться"
        driver.find_element(*Locators.TEXT_REGISTRATION).click()

        # Вводим данные для регистрации
        driver.find_element(*Locators.REG_NAME).send_keys(Constants.NAME)
        driver.find_element(*Locators.AUTH_EMAIL).send_keys(new_email)
        driver.find_element(*Locators.AUTH_PASSWORD).send_keys(Constants.TEST_PASSWORD)

        # Клик по кнопке "Зарегистрироваться"
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()

        WebDriverWait(driver, 10).until(EC.url_contains(Constants.LOGIN_URL))
        assert '/login' in driver.current_url
