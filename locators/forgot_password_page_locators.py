from selenium.webdriver.common.by import By

class ForgotPasswordPageLocators:
    EMAIL_INPUT = (By.XPATH, '//input[@type="text" and @name="name"]')
    RESET_BUTTON = (By.XPATH, '//button[text()="Восстановить"]')