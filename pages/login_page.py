from .base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from .forgot_password_page import ForgotPasswordPage
from utils.config import LOGIN_PAGE_URL

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginPageLocators()

    def open(self):
        """Переходим на страницу логина."""
        self.driver.get(LOGIN_PAGE_URL)
    
    def click_forgot_password_link(self):
        """Кликаем на ссылку 'Восстановить пароль'."""
        self.js_click(self.locators.FORGOT_PASSWORD_LINK)
        return ForgotPasswordPage(self.driver)
    
    def login(self, email, password):
        """Авторизация с использованием email и пароля."""
        self.enter_text(self.locators.EMAIL_INPUT, email)
        self.enter_text(self.locators.PASSWORD_INPUT, password)
        self.js_click(self.locators.LOGIN_BUTTON)