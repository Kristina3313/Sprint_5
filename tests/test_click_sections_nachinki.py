from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class TestClickSections:
    def test_active_tab_nachinki_pisitive(self, driver):
        # Клик на раздел "Начинки"
        driver.find_element(*Locators.NACHINKI).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ACTIVE_TAB))

        # Проверка, что раздел "Начинки" активен
        assert driver.find_element(*Locators.ACTIVE_TAB).text == 'Начинки'

