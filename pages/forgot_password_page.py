from .base_page import BasePage
from locators.forgot_password_page_locators import ForgotPasswordPageLocators

class ForgotPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ForgotPasswordPageLocators()

    def enter_email(self, email):
        """Ввод email в поле."""
        self.enter_text(self.locators.EMAIL_INPUT, email)

    def click_recover_button(self):
        """Клик на кнопку 'Восстановить'."""
        self.js_click(self.locators.RESET_BUTTON)