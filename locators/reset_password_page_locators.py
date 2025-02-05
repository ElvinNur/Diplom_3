from selenium.webdriver.common.by import By

class ResetPasswordPageLocators:
    PASSWORD_FIELD = (By.XPATH, '//input[@type="password" and @name="Введите новый пароль"]')
    TOGGLE_BUTTON = (By.CSS_SELECTOR, 'svg[width="24"][height="24"][fill="#F2F2F3"][viewBox="0 0 24 24"] path')
    PASSWORD_LABEL = (By.CSS_SELECTOR, "label.input__placeholder-focused")
    