from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants
from locators import Locators

class Test:
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

        driver.quit()
