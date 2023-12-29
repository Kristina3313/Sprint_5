from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants
from locators import Locators


class TestRegistration:
    def test_registration_wrong_password(self, driver):
        # Клик по кнопке "Войти в аккаунт"
        driver.find_element(*Locators.BUTTON_PESONAL_ACCOUNT).click()

        WebDriverWait(driver, 5).until(EC.url_contains(Constants.LOGIN_URL))

        # Клик по тексту "Зарегистрироваться"
        driver.find_element(*Locators.TEXT_REGISTRATION).click()

        # Ввод данных
        driver.find_element(*Locators.AUTH_EMAIL).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.AUTH_PASSWORD).send_keys(Constants.WRONG_PASSWORD)
        driver.find_element(*Locators.REG_NAME).send_keys(Constants.NAME)

        # Клик по кнопке "Зарегистрироваться"
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()

        # Явное ожидание появления элемента
        wrong_locator = Locators.WRONG_MESSAGE
        wrong = WebDriverWait(driver, 10).until(EC.presence_of_element_located(wrong_locator))

        # Проверяем, что текст соответствует ошибке
        assert wrong.text == 'Некорректный пароль'
