from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants
from locators import Locators


class TestLogin:
    def test_login_from_button_main_page_positive(self, driver):
        # Клик по кнопке "Войти в аккаунт"
        driver.find_element(*Locators.BUTTON_PESONAL_ACCOUNT).click()

        WebDriverWait(driver, 5).until(EC.url_contains(Constants.LOGIN_URL))

        # Вход в личный кабинет
        driver.find_element(*Locators.AUTH_EMAIL).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.AUTH_PASSWORD).send_keys(Constants.TEST_PASSWORD)

        # Клик на кнопке "Вход"
        driver.find_element(*Locators.BUTTON_LOGIN).click()

        # Ждем, пока кнопка "Оформить заказ" станет видимой после авторизации
        button_text = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.BUTTON_PLACE_ORDER)).text
        assert button_text == "Оформить заказ"


    def test_login_from_password_recovery_positive(self, driver):
        # Клик по кнопке "Войти в аккаунт"
        driver.find_element(*Locators.BUTTON_PESONAL_ACCOUNT).click()

        WebDriverWait(driver, 5).until(EC.url_contains(Constants.LOGIN_URL))

        # Клик по тексту "Восстановить пароль"
        driver.find_element(*Locators.TEXT_RECOVERY).click()

        WebDriverWait(driver, 5).until(EC.url_contains(Constants.URL_RECOVERY_PASSWORD))

        # Заполняем форму восстановления пароля
        driver.find_element(*Locators.AUTH_EMAIL).send_keys(Constants.TEST_EMAIL)

        # Клик на кнопку "Восстановить"
        driver.find_element(*Locators.BUTTON_RECOVERY).click()

        WebDriverWait(driver, 10).until(EC.url_contains(Constants.URL_RESET_PASSWORD))
        # Проверка, что URL соответствует странице
        assert 'reset-password' in driver.current_url


    def test_login_from_personal_account_positive(self, driver):
        # Клик по кнопке "Личный кабинет"
        driver.find_element(*Locators.BUTTON_LOGIN_ACCOUNT).click()

        WebDriverWait(driver, 5).until(EC.url_contains(Constants.LOGIN_URL))

        # Вводим данные для авторизации
        driver.find_element(*Locators.AUTH_EMAIL).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.AUTH_PASSWORD).send_keys(Constants.TEST_PASSWORD)

        # Клик на кнопке "Вход"
        driver.find_element(*Locators.BUTTON_LOGIN).click()

        # Ждем, пока кнопка "Оформить заказ" станет видимой после авторизации
        button_text = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.BUTTON_PLACE_ORDER)).text
        assert button_text == "Оформить заказ"


    def test_login_from_registration_form_positive(self, driver):
        # Клик по кнопке "Войти в аккаунт"
        driver.find_element(*Locators.BUTTON_PESONAL_ACCOUNT).click()

        WebDriverWait(driver, 5).until(EC.url_contains(Constants.LOGIN_URL))

        # Клик по тексту "Зарегистрироваться"
        driver.find_element(*Locators.TEXT_REGISTRATION).click()

        # Клик по кнопке "Войти" на странице регистрации
        driver.find_element(*Locators.TEXT_LOGIN).click()

        # Вход в личный кабинет
        driver.find_element(*Locators.AUTH_EMAIL).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.AUTH_PASSWORD).send_keys(Constants.TEST_PASSWORD)

        # Клик на кнопке "Вход"
        driver.find_element(*Locators.BUTTON_LOGIN).click()

        # Ждем пока кнопка "Оформить заказ" станет видимой после авторизации
        button_text = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.BUTTON_PLACE_ORDER)).text
        assert button_text == "Оформить заказ"
