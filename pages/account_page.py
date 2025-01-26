from .base_page import BasePage
from locators.account_page_locators import AccountPageLocators
from locators.login_page_locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config import LOGIN_PAGE_URL, PROFILE_PAGE_URL, ORDER_HISTORY_PAGE_URL

class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = AccountPageLocators()

    def verify_profile_page_loaded(self):
        """Проверяем, что страница профиля загружена."""
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.current_url == PROFILE_PAGE_URL
        )
        assert self.is_correct_url(PROFILE_PAGE_URL), \
            "Не удалось загрузить страницу профиля"

    def go_to_order_history(self):
        """Переход в раздел 'История заказов'."""
        self.js_click(self.locators.ORDER_HISTORY_BUTTON)
        assert self.is_correct_url(ORDER_HISTORY_PAGE_URL), \
            "Не удалось загрузить страницу 'История заказов'"

    def logout(self):
        """Выход из аккаунта."""
        self.js_click(self.locators.LOGOUT_BUTTON)

        # Ожидание появления кнопки "Войти"
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        )

        # Проверка правильного URL
        assert self.is_correct_url(LOGIN_PAGE_URL), \
            "Не удалось выйти из аккаунта"