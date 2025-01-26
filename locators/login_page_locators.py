from selenium.webdriver.common.by import By

class LoginPageLocators:

    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, "a[href='/forgot-password']")
    EMAIL_INPUT = (By.XPATH, '//input[@type="text" and @name="name"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@type="password" and @name="Пароль"]')
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти"]')