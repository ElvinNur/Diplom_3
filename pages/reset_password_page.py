from .base_page import BasePage
from locators.reset_password_page_locators import ResetPasswordPageLocators

class ResetPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ResetPasswordPageLocators()

    def toggle_password_visibility(self):
        """Кликаем на кнопку показать/скрыть пароль."""
        self.js_click(self.locators.TOGGLE_BUTTON)

    def verify_password_field_active(self):
        """Проверяем, что поле пароля становится активным."""
        password_label = self.find_element(self.locators.PASSWORD_LABEL)
        assert "input__placeholder-focused" in password_label.get_attribute("class"), \
            "Поле пароля не стало активным!"

    def verify_reset_password_page_loaded(self):
        """Проверяем, что страница сброса пароля загружена."""
        assert self.is_element_visible(self.locators.PASSWORD_FIELD), \
            "Страница сброса пароля не загрузилась."