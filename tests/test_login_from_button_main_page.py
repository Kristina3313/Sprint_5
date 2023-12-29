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
