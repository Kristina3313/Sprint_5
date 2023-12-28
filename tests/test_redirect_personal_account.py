from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants
from locators import Locators

class Test:
    def test_redirect_personal_account_positive(self, driver):
        # Клик по кнопке "Войти в аккаунт"
        driver.find_element(*Locators.BUTTON_PESONAL_ACCOUNT).click()

        WebDriverWait(driver, 5).until(EC.url_contains(Constants.LOGIN_URL))

        # Вход в личный кабинет
        driver.find_element(*Locators.AUTH_EMAIL).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.AUTH_PASSWORD).send_keys(Constants.TEST_PASSWORD)

        # Клик на кнопке "Вход"
        driver.find_element(*Locators.BUTTON_LOGIN).click()

        WebDriverWait(driver, 5).until(EC.url_contains(Constants.URL))

        # Переход в личный кабинет
        driver.find_element(*Locators.BUTTON_LOGIN_ACCOUNT).click()

        WebDriverWait(driver, 5).until(EC.url_contains(Constants.URL_PROFILE))

        # Проверка, что открыта страница личного кабинета по URL
        WebDriverWait(driver, 10).until(EC.url_contains(Constants.URL_PROFILE))
        assert 'account/profile' in driver.current_url

        driver.quit()
