from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants
from locators import Locators

class Test:
    def test_redirect_to_construktor_positive(self, driver):
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

        # Переход по клику на "Конструктор"
        driver.find_element(*Locators.BUTTON_CONSTRUKTOR).click()

        # Проверяем элемент конструктора отображается на странице
        element = driver.find_element(By.CLASS_NAME, "BurgerIngredients_ingredients__1N8v2")
        assert element.is_displayed()

        driver.quit()
