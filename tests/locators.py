from selenium.webdriver.common.by import By


class Locators():
    # Локатор для ввода почты на странице авторизации
    AUTH_EMAIL = (By.XPATH, "//label[text()='Email']//following-sibling::input[@name='name']")
    # Локатор для ввода пароля на странице авторизации
    AUTH_PASSWORD = (By.XPATH, "//label[text()='Пароль']//following-sibling::input[@name='Пароль']")
    # Локатор для ввода Имени на странице Регистрации
    REG_NAME = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    # Кнопка "Войти в аккаунт"
    BUTTON_PESONAL_ACCOUNT = (By.XPATH, "// button[text() = 'Войти в аккаунт']")
    # Кнопка "Вход" на странице /login
    BUTTON_LOGIN = (By.XPATH,"//button[text()='Войти']")
    # Кнопка "Оформить заказ"
    BUTTON_PLACE_ORDER = (By.XPATH,"// button[text() = 'Оформить заказ']")
    # Текст "Восстановить пароль"
    TEXT_RECOVERY = (By.XPATH,"//a[@href='/forgot-password']")
    # Кнопка "Восстановить"
    BUTTON_RECOVERY = (By.XPATH, "//button[text()='Восстановить']")
    # Кнопка "Личный кабинет"
    BUTTON_LOGIN_ACCOUNT = (By.XPATH, "//a[@class='AppHeader_header__link__3D_hX']//p[text()='Личный Кабинет']")
    # Кнопка "Выход"
    BUTTON_LOGOUT = (By.XPATH, "//button[text()='Выход']")
    # Лого "StellarBurger"
    LOGO_STELLARURGER = (By.XPATH, "//header/nav[1]/div[1]/a[1]/*[1]")
    # Кнопка "Конструктор"
    BUTTON_CONSTRUKTOR = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    # Текст "Зарегистрироваться"
    TEXT_REGISTRATION = (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")
    # Текст "Войти" на странице регистрации
    TEXT_LOGIN = (By.XPATH, "// a[contains(text(), 'Войти')]")
    # Кнопка "Зарегистрироваться"
    BUTTON_REGISTRATION = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")
    # Ошибка "Некорректный пароль"
    WRONG_MESSAGE = (By.XPATH, "// p[contains(text(), 'Некорректный пароль')]")
    # Раздел "Соусы"
    SAUSE = (By.XPATH, '// span[contains(text(), "Соусы")]')
    # Раздел "Булки"
    BULKI = (By.XPATH, '//span[contains(text(), "Булки")]')
    # Раздел "Начинки"
    NACHINKI = (By.XPATH, "//span[contains(text(), 'Начинки')]")
    # Активный таб
    ACTIVE_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]")
