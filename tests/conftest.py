import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import Constants
from locators import Locators


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(Constants.URL)
    yield driver
    driver.quit()

# Фикстура для авторизации
def login(driver):
    driver.find_element(*Locators.AUTH_EMAIL).send_keys(Constants.TEST_EMAIL)
    driver.find_element(*Locators.AUTH_PASSWORD).send_keys(Constants.TEST_PASSWORD)
    driver.find_element(*Locators.BUTTON_LOGIN).click()
    yield driver






